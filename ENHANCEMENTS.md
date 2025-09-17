# Enhancements & Optimization Ideas

A living document to track ideas for improving efficiency and reducing costs in the Business Impact Simulator project.

## Efficiency Improvements
- [ ] **Batch LLM Requests:** Refactor the DomainClassifier so it can classify multiple projects in a single API call, instead of one call per project. This could significantly reduce API costs and improve throughput.
- [ ] **Async Processing:** Implement asynchronous task execution for faster throughput.
- [ ] **Cache Results:** Cache classification results for repeated or similar projects.

## Cost Optimization
- [ ] **Model Selection:** Explore using cheaper LLM models for less critical tasks.
- [ ] **Request Minimization:** Minimize prompt length and frequency to reduce token usage.
- [ ] **Open-Source Alternatives:** Evaluate open-source LLMs for local inference.

## Other Ideas
- [ ] **Monitoring:** Add logging to track API usage and costs over time.
- [ ] **User Feedback:** Collect user feedback on classification accuracy to improve prompts.
- [ ] **Industry Database:** Implement a database to store and manage industry data, allowing the system to update and incorporate new or emerging industries dynamically.
- [ ] **Prompt for Missing Project Fields:** When `ProjectParser` final dictionary preparation removes keys with empty values, detect the missing fields and prompt the user to enter string values for those fields (e.g., `Industries`, `Tags`, `Project Type`, `Technologies Used`, `Stakeholders`, `Objectives`, `Location`, `Regulatory Context`).
- [ ] **Multimedia Upload Support:** Extend file upload to accept video (.mp4) and audio (.mp3) files, with transcription/analysis capabilities for project descriptions.
- [ ] **Voice Input:** Add microphone functionality to the input dialog, allowing users to verbally describe their project for automatic transcription and processing.
- [ ] **WebSocket Communication:** Implement real-time communication between frontend and backend for streaming responses and live updates.
- [ ] **Server-Side Rendering:** Render React components on the Python server for simpler architecture and better SEO.
- [ ] **Desktop Application:** Package the entire system as an Electron app for offline use and direct Python-React communication.
- [ ] **Unified Input Endpoint:** Add a single endpoint that accepts both text and file in one request (multipart form-data with optional `description` and `file`) to simplify the frontend flow once separate endpoints are working.

---

*Add new ideas below!*