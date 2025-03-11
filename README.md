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
For small changed editing the files directly on Github should be sufficient. However, for larger changes you may want to 
build the site locally and preview your changes befoe committing them to the `main` branch. If you want to build the 
site locally:

1. Clone this repository
2. Install the required dependencies: `pip install -r requirements.txt`
3. Build the site using Pelican: `pelican`
4. Start the development server: `pelican --listen`

## Adding a Page

1. Create a new HTML file in the `content/pages` directory. It's probably easiest to copy an existing file and modify it as needed.
2. Make sure that the file has a `<title>` tag in the `<head>` section. This title will be used to generate the slug and as the title displayed at the top of the page.
3. Anything inside the `<body>` tag will be used as the content of the page.

## Adding a Blog Post

1. Create a new HTML file in the `content/blog` directory. It's probably easiest to copy an existing file and modify it as needed.
2. Make sure that the file has a `<title>` tag in the `<head>` section. This title will be used to generate the slug and as the title displayed at the top of the post.
3. make sure the file has a `<meta name="date" content="YYYY-MM-DD HH:MM:SS" />` tag in the `<head>` section. This date will be used to sort the posts.
4. You may want to include an `<meta name="authors" content="Author Name" />` tag in the `<head>` section. This will be used to display the author of the post.
5. Anything inside the `<body>` tag will be used as the content of the post.

## Customizing Pages / Posts

1. If you need the page to use a different, specific slug, you can override the default slug by providing a `<meta>` tag with the name `save_as` and the desired file name as the content. For example: `<meta name="save_as" content="my-slug.html" />`
2. If you need to use a custom template to make a particular page look different, you can override the default by providing a `<meta>` tag with the name `template` and the desired template name as the content. For example: `<meta name="template" content="custom-template" />`
