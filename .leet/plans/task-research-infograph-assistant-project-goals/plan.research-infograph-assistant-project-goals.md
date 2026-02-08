---
task_name: research-infograph-assistant-project-goals
status: pending
created_at: '2026-02-08T17:08:12Z'
updated_at: '2026-02-08T17:08:12Z'
source_task: task.md
source_hash: ad24712112ec9417f1b9e0a6a2bb57b69846e3d0c6c2fb3530fe60016868554e
---

# Task: research-infograph-assistant-project-goals

## Description

# Research Infograph Assistant - Project Goals

## Subtasks

### 1. Tasks:**

Tasks:**

### 2. Initialize Python package structure under `backend/src/infograph/`

Initialize Python package structure under `backend/src/infograph/`

### 3. Create `main.py` with Click CLI for starting server

Create `main.py` with Click CLI for starting server

### 4. Create `api_service.py` with FastAPI app, CORS middleware

Create `api_service.py` with FastAPI app, CORS middleware

### 5. Create `health_router.py` with `/api/v1/health` endpoint

Create `health_router.py` with `/api/v1/health` endpoint

### 6. Add `pyproject.toml` with dependencies

Add `pyproject.toml` with dependencies

### 7. Acceptance Criteria:**

Acceptance Criteria:**

### 8. `python -m infograph.svc.main --port 8000` starts the server

`python -m infograph.svc.main --port 8000` starts the server

### 9. `GET http://localhost:8000/api/v1/health` returns `{"status": "ok"}`

`GET http://localhost:8000/api/v1/health` returns `{"status": "ok"}`

### 10. pytest test passes for health endpoint

pytest test passes for health endpoint

### 11. Tasks:**

Tasks:**

### 12. Initialize Vite + Vue 3 project

Initialize Vite + Vue 3 project

### 13. Configure TailwindCSS and Element Plus

Configure TailwindCSS and Element Plus

### 14. Create router with placeholder pages (Login, Chat, History)

Create router with placeholder pages (Login, Chat, History)

### 15. Create `request.js` Axios instance pointing to backend

Create `request.js` Axios instance pointing to backend

### 16. Create health check API call on app load

Create health check API call on app load

### 17. Acceptance Criteria:**

Acceptance Criteria:**

### 18. `yarn dev` starts frontend on port 3001

`yarn dev` starts frontend on port 3001

### 19. App shows "Backend Connected" status on successful health check

App shows "Backend Connected" status on successful health check

### 20. Router navigates between placeholder pages

Router navigates between placeholder pages

### 21. Tasks:**

Tasks:**

### 22. Create abstract store interfaces for User, Session, Source, Infographic, Message

Create abstract store interfaces for User, Session, Source, Infographic, Message

### 23. Implement DuckDB stores following `DuckDBClient` patterns

Implement DuckDB stores following `DuckDBClient` patterns

### 24. Create tables with proper schemas

Create tables with proper schemas

### 25. Write pytest tests for CRUD operations

Write pytest tests for CRUD operations

### 26. Acceptance Criteria:**

Acceptance Criteria:**

### 27. Can create, read, update, delete all entity types

Can create, read, update, delete all entity types

### 28. All store tests pass

All store tests pass

### 29. Tables created automatically on first use

Tables created automatically on first use

### 30. Tasks:**

Tasks:**

### 31. Backend: Create `auth_service.py` to verify Google tokens

Backend: Create `auth_service.py` to verify Google tokens

### 32. Backend: Create `auth_router.py` with `/auth/google` and `/auth/me` endpoints

Backend: Create `auth_router.py` with `/auth/google` and `/auth/me` endpoints

### 33. Backend: Generate JWT tokens for authenticated sessions

Backend: Generate JWT tokens for authenticated sessions

### 34. Frontend: Create `LoginPage.vue` with Google Sign-In button

Frontend: Create `LoginPage.vue` with Google Sign-In button

### 35. Frontend: Create `useAuth.js` composable for auth state

Frontend: Create `useAuth.js` composable for auth state

### 36. Frontend: Create `auth` Pinia store

Frontend: Create `auth` Pinia store

### 37. Frontend: Add auth guard to router

Frontend: Add auth guard to router

### 38. Acceptance Criteria:**

Acceptance Criteria:**

### 39. User can click "Sign in with Google" button

User can click "Sign in with Google" button

### 40. After Google auth, user is redirected to Chat page

After Google auth, user is redirected to Chat page

### 41. User info (name, email) is displayed in header

User info (name, email) is displayed in header

### 42. Unauthenticated users are redirected to Login page

Unauthenticated users are redirected to Login page

### 43. JWT token stored in localStorage, sent with API requests

JWT token stored in localStorage, sent with API requests

### 44. Tasks:**

Tasks:**

### 45. Backend: Create `session_router.py` with all session endpoints

Backend: Create `session_router.py` with all session endpoints

### 46. Backend: Implement session store operations

Backend: Implement session store operations

### 47. Frontend: Create session Pinia store

Frontend: Create session Pinia store

### 48. Frontend: Add "New Research" button on Chat page

Frontend: Add "New Research" button on Chat page

### 49. Frontend: Create `HistoryPage.vue` with session list

Frontend: Create `HistoryPage.vue` with session list

### 50. Acceptance Criteria:**

Acceptance Criteria:**

### 51. User can create a new research session with a prompt

User can create a new research session with a prompt

### 52. User can see list of their sessions on History page

User can see list of their sessions on History page

### 53. User can click a session to view details

User can click a session to view details

### 54. User can delete a session

User can delete a session

### 55. Tasks:**

Tasks:**

### 56. Backend: Create message endpoints in `session_router.py`

Backend: Create message endpoints in `session_router.py`

### 57. Frontend: Create `ChatPage.vue` with full chat interface

Frontend: Create `ChatPage.vue` with full chat interface

### 58. Frontend: Create `ChatInput.vue` component

Frontend: Create `ChatInput.vue` component

### 59. Frontend: Create `MessageList.vue` and `MessageBubble.vue`

Frontend: Create `MessageList.vue` and `MessageBubble.vue`

### 60. Frontend: Create chat Pinia store

Frontend: Create chat Pinia store

### 61. Acceptance Criteria:**

Acceptance Criteria:**

### 62. User can type and send messages

User can type and send messages

### 63. Messages appear in chat history

Messages appear in chat history

### 64. Chat scrolls to latest message

Chat scrolls to latest message

### 65. Loading indicator while waiting for response

Loading indicator while waiting for response

### 66. Tasks:**

Tasks:**

### 67. Backend: Create `search_service.py` with web search capability

Backend: Create `search_service.py` with web search capability

### 68. Backend: Parse search results into Source objects

Backend: Parse search results into Source objects

### 69. Backend: Store sources linked to session

Backend: Store sources linked to session

### 70. Backend: Create `source_router.py` endpoints

Backend: Create `source_router.py` endpoints

### 71. Frontend: Create `SourceList.vue` and `SourceCard.vue`

Frontend: Create `SourceList.vue` and `SourceCard.vue`

### 72. Frontend: Display sources in session detail

Frontend: Display sources in session detail

### 73. Acceptance Criteria:**

Acceptance Criteria:**

### 74. When user submits a research prompt, web search is triggered

When user submits a research prompt, web search is triggered

### 75. Sources are extracted and stored

Sources are extracted and stored

### 76. Source list shows title, URL, snippet, confidence

Source list shows title, URL, snippet, confidence

### 77. Clicking source opens URL in new tab

Clicking source opens URL in new tab

### 78. Tasks:**

Tasks:**

### 79. Backend: Create `infographic_service.py` with template-based generation

Backend: Create `infographic_service.py` with template-based generation

### 80. Backend: Create basic template (title, key points, sources)

Backend: Create basic template (title, key points, sources)

### 81. Backend: Generate PNG image and save to filesystem

Backend: Generate PNG image and save to filesystem

### 82. Backend: Create `infographic_router.py` endpoints

Backend: Create `infographic_router.py` endpoints

### 83. Frontend: Create `InfographicViewer.vue` component

Frontend: Create `InfographicViewer.vue` component

### 84. Frontend: Display infographic in session detail

Frontend: Display infographic in session detail

### 85. Acceptance Criteria:**

Acceptance Criteria:**

### 86. After sources are gathered, infographic is auto-generated

After sources are gathered, infographic is auto-generated

### 87. Infographic shows title (from prompt), key bullet points, source count

Infographic shows title (from prompt), key bullet points, source count

### 88. PNG image displays in session detail page

PNG image displays in session detail page

### 89. Image path stored in database

Image path stored in database

### 90. Tasks:**

Tasks:**

### 91. Backend: Add query params to list sessions (date range, search)

Backend: Add query params to list sessions (date range, search)

### 92. Frontend: Add date picker and search input to History page

Frontend: Add date picker and search input to History page

### 93. Frontend: Add pagination

Frontend: Add pagination

### 94. Acceptance Criteria:**

Acceptance Criteria:**

### 95. User can filter sessions by date range

User can filter sessions by date range

### 96. User can search sessions by prompt text

User can search sessions by prompt text

### 97. Pagination works for large session lists

Pagination works for large session lists

### 98. Tasks:**

Tasks:**

### 99. Backend: Add export endpoint returning JSON or ZIP

Backend: Add export endpoint returning JSON or ZIP

### 100. Backend: Support PNG and SVG export for infographic

Backend: Support PNG and SVG export for infographic

### 101. Frontend: Create `InfographicExport.vue` with download buttons

Frontend: Create `InfographicExport.vue` with download buttons

### 102. Frontend: Add export buttons to session detail

Frontend: Add export buttons to session detail

### 103. Acceptance Criteria:**

Acceptance Criteria:**

### 104. User can download infographic as PNG

User can download infographic as PNG

### 105. User can download infographic as SVG

User can download infographic as SVG

### 106. User can download session data as JSON

User can download session data as JSON

### 107. ZIP option includes infographic + sources + metadata

ZIP option includes infographic + sources + metadata

### 108. Tasks:**

Tasks:**

### 109. Backend: Add template selection to infographic generation

Backend: Add template selection to infographic generation

### 110. Backend: Implement "stats" template with bar/pie charts

Backend: Implement "stats" template with bar/pie charts

### 111. Backend: Implement "timeline" template

Backend: Implement "timeline" template

### 112. Frontend: Add template selector in session detail

Frontend: Add template selector in session detail

### 113. Frontend: Regenerate infographic with new template

Frontend: Regenerate infographic with new template

### 114. Acceptance Criteria:**

Acceptance Criteria:**

### 115. User can choose from 3 templates: basic, stats, timeline

User can choose from 3 templates: basic, stats, timeline

### 116. Stats template includes at least one chart

Stats template includes at least one chart

### 117. Timeline template shows chronological info

Timeline template shows chronological info

### 118. Regenerate button creates new infographic

Regenerate button creates new infographic

### 119. JWT tokens expire after 24 hours

JWT tokens expire after 24 hours

### 120. API endpoints validate JWT on every request

API endpoints validate JWT on every request

### 121. Google OAuth client ID stored in environment variable

Google OAuth client ID stored in environment variable

### 122. No secrets committed to repository

No secrets committed to repository

### 123. API responses under 500ms for CRUD operations

API responses under 500ms for CRUD operations

### 124. Infographic generation under 30 seconds

Infographic generation under 30 seconds

### 125. Frontend initial load under 2 seconds

Frontend initial load under 2 seconds

### 126. All interactive elements keyboard accessible

All interactive elements keyboard accessible

### 127. ARIA labels on buttons and inputs

ARIA labels on buttons and inputs

### 128. Color contrast meets WCAG AA

Color contrast meets WCAG AA

### 129. All UI strings in i18n files

All UI strings in i18n files

### 130. Support English, Japanese, Chinese

Support English, Japanese, Chinese

### 131. Date/time formatted per locale

Date/time formatted per locale

### 132. Unit tests for each store (CRUD operations)

Unit tests for each store (CRUD operations)

### 133. Unit tests for each service (auth, search, infographic)

Unit tests for each service (auth, search, infographic)

### 134. Integration tests for each router endpoint

Integration tests for each router endpoint

### 135. Run: `pytest tests/ -v`

Run: `pytest tests/ -v`

### 136. Component tests for key components

Component tests for key components

### 137. E2E smoke test for login flow

E2E smoke test for login flow

### 138. Run: `yarn test`

Run: `yarn test`

### 139. All 11 goals are implemented and tested

All 11 goals are implemented and tested

### 140. User can sign in, create research, view infographic, and export

User can sign in, create research, view infographic, and export

### 141. All pytest tests pass

All pytest tests pass

### 142. Frontend builds without errors

Frontend builds without errors

### 143. README documents all features and setup instructions

README documents all features and setup instructions
