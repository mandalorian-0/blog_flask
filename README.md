# Blog Flask

A modern, responsive blog application built with Flask that fetches and displays blog posts from an external API. Features a clean UI with Markdown support for rich content formatting.

## 🚀 Features

- **Dynamic Content Loading**: Fetches blog posts from an external API
- **Markdown Support**: Renders blog post content with full Markdown formatting
- **Responsive Design**: Mobile-first design that looks great on all devices
- **Post Management**: Individual post pages with breadcrumb navigation
- **Reading Time Estimation**: Automatically calculates reading time for each post
- **Modern UI**: Clean, gradient-based design with smooth animations
- **Post Caching**: Optimized performance with in-memory post caching
- **SEO-Friendly**: Proper meta tags and semantic HTML structure

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/mandalorian-0/blog_flask.git
   cd blog_flask
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## ⚙️ Configuration

The application uses an external API to fetch blog posts. The API endpoint is configured in `config.py`:

```python
API_URL = "https://api.npoint.io/f988fe2f89471cfb558e"
```

To use your own blog data, update this URL to point to your API endpoint. The API should return JSON data with the following structure:

```json
[
  {
    "title": "Post Title",
    "slug": "post-title",
    "author": "Author Name",
    "description": "Short description",
    "body": "Full post content in Markdown",
    "created_at": "2024-01-01T12:00:00.000"
  }
]
```

## 🚀 Running the Application

1. **Start the Flask development server**
   ```bash
   python main.py
   ```

2. **Access the application**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/blog
   ```

## 📁 Project Structure

```
blog_flask/
├── main.py                 # Application entry point
├── config.py              # Configuration settings
├── post.py                # Post model class
├── requirements.txt       # Project dependencies
├── routes/
│   └── blog_routes.py    # Blog route handlers
├── services/
│   ├── api_service.py    # External API integration
│   └── post_service.py   # Post processing and caching
├── templates/
│   ├── index.html        # Home page with post grid
│   └── post.html         # Individual post page
└── static/
    └── assets/
        └── css/
            └── styles.css # Application styles
```

## 🎨 Key Components

### Routes (`routes/blog_routes.py`)
- `/blog` - Homepage displaying all blog posts
- `/blog/posts/<slug>` - Individual post page

### Services
- **`api_service.py`**: Handles fetching data from the external API
- **`post_service.py`**: Processes posts, converts Markdown to HTML, formats dates, and manages caching

### Templates
- **`index.html`**: Homepage with responsive grid layout of blog cards
- **`post.html`**: Individual post view with breadcrumb navigation and social sharing

## 📦 Dependencies

Key dependencies include:
- **Flask 3.1.2**: Web framework
- **Markdown 3.10**: Markdown to HTML conversion
- **requests 2.32.5**: HTTP library for API calls
- **Jinja2 3.1.6**: Template engine (included with Flask)

See `requirements.txt` for the complete list.

## 🎯 Features in Detail

### Post Processing
- Converts Markdown content to HTML
- Formats dates to a readable format (e.g., "Monday 01, 2024")
- Calculates reading time based on word count
- Caches processed posts for better performance

### UI/UX
- Sticky navigation bar
- Hero section with search bar (visual placeholder)
- Animated card transitions
- Responsive grid layout (1 column on mobile, 2 on tablet, 3 on desktop)
- Social sharing buttons
- Footer with social links

## 🔧 Development

To run the application in debug mode:

```python
# main.py already has debug=True configured
app.run(debug=True)
```

Debug mode enables:
- Automatic reloading on code changes
- Detailed error messages
- Interactive debugger

## 🚀 Production Deployment

For production deployment, consider:

1. **Disable debug mode**:
   ```python
   app.run(debug=False)
   ```

2. **Use a production WSGI server** like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn main:app
   ```

3. **Set environment variables** for sensitive configuration
4. **Use a reverse proxy** like Nginx
5. **Enable HTTPS** for secure connections

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Mandalorian**

- GitHub: [@mandalorian-0](https://github.com/mandalorian-0)

## 🙏 Acknowledgments

- Built with Flask
- UI inspired by modern blog designs
- Markdown rendering powered by Python-Markdown

---

Made with ♥️ by Mandalorian
