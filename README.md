# GenePattern Website

This repository contains the source code for the GenePattern website. It is built using 
[Pelican](https://docs.getpelican.com), a Python static site generator. 

To update the website, all you need to do is to update the content in the `content` directory and push your changes to 
the `main` branch. The website will then be automatically updated via Github action.

## Structure

* **content:** Contains the source files for the website. Each page is written in HTML format.
    - **blog:** Contains the blog posts.
    - **modules:** Contains the module documentation pages.
    - **pages:** Contains the main pages of the website.
    - **uploaded:** Contains the uploaded images and other files to embed in the website.
* **theme:** Contains the Pelican theme for the website.
    - **static:** Contains css, js, images and other static files for the theme.
    - **templates:** Contains the Jinja2 templates for the theme.
* **pelicanconf.py:** Contains the configuration for Pelican.

## Development
If you want to build the site locally:

1. Clone this repository
2. Install the required dependencies: `pip install -r requirements.txt`
3. Build the site using Pelican: `pelican`
4. Start the development server: `pelican --listen`