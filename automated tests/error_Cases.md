Azure OpenAI chat completions uses HTTP status codes to indicate success or failure, with detailed JSON error bodies for the specified cases.

## Response Explanations

### 200 OK (normal)
**Success response for valid requests.** Contains the generated completion in `choices[0].message.content`, along with metadata like `id`, `model`, token `usage`, and `finish_reason` ("stop" for normal completion). This is the expected response when your prompt, model deployment, and parameters are correct. [developers.openai](https://developers.openai.com/cookbook/examples/azure/chat/)

### 400 Bad Request (content_filter)
**Request blocked by Azure's content moderation filters.** Triggered when prompt or generated response violates policies (hate speech, violence, sexual content). The `innererror.content_filter_result` shows filtered categories and severity levels. No completion returned - revise prompt to comply. [learn.microsoft](https://learn.microsoft.com/en-us/azure/ai-foundry/openai/concepts/content-filter?view=foundry-classic)

### 400 Bad Request (invalid_request)
**Malformed or invalid request parameters.** Common causes: unsupported model for endpoint, invalid JSON syntax, missing required fields (like `messages`), exceeding token limits, or incorrect data types. Fix by validating request body against API schema. [community.openai](https://community.openai.com/t/error-retrieving-completions-400-bad-request/34004)

### 429 Rate Limit
**Exceeded quota limits (TPM/RPM).** Tokens Per Minute (TPM) or Requests Per Minute (RPM) quota breached for your deployment/subscription. Response includes retry guidance. Implement exponential backoff and check Azure quota settings. [community.openai](https://community.openai.com/t/openai-chat-list-of-error-codes-and-types/357791)

### 500 Internal Server
**Azure service-side failure.** Temporary backend issues, model overload, or infrastructure problems. Not your fault - retry after delay. Frequent 500s may indicate quota exhaustion or regional capacity limits; monitor Azure metrics. [learn.microsoft](https://learn.microsoft.com/en-us/answers/questions/2180486/azure-openai-api-internal-server-error-(500)-on-ch)