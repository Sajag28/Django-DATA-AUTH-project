This is the project which is my medium to django development which is a way for me to go towards side of MLOps. Currently there is an underprogress project
Apps:

authentication: Customizes user registration, login, and logout, if needed.
content: Manages creation, storage, retrieval, and modification of content.
messages: Integrates the Django message framework for user feedback.
Models:

User: Extends the default user model with additional fields or custom logic.
Content: Represents the specific content type(s) with appropriate fields.
Views:

Handles form submissions and data processing for non-GET requests.
Renders dynamic content and templates according to user interactions.
Implements authentication checks for protected views.
Templates:

Provides HTML structure and integrates Django template tags/filters.
Displays forms, error messages, and dynamic content.
Middleware:

