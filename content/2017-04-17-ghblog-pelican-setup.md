Title: Setting up a GitHub blog with Pelican
Date: 2017-04-17
Category: Blogging
Tags: pelican, markdown, ghpages

I've been thinking about writing my own Blog for a long time, but had not found the time to invest into searching the simple and fun kind of solution I was looking for.
Not being a developer, I only discovered very recently that GitHub is offering a free way of hosting your own static blog.
I was quickly interested, and a few minutes googling pointed me to [Jekyllrb](http://jekyllrb.com) as the natural tool to build my static site and have it hosted as a GitHub user page.
But I was not fully convinced at start because I wasn't willing to invest in learning Ruby. So it took me a bit more googling to find [pelican](http://getpelican.com), which is a [Python](http://python.org) tool, a language I'm more comfortable with.

Here's how I have set up Pelican in order to be able to publish my Blog on My GitHub User Page:

### Setup your User Page repo on GitHub
Simply create a new GitHub repository named `<github-user-name>.github.io`.
You can follow the instructions [here](https://pages.github.com).


### Install & Setup Pelican on your PC
I'm Assuming you already have Python installed (As of today, Pelican works as nicely with Python 2.7.x as with 3.3+).
If this is not the case and if you're working on WindowsTM, I recommend using [Chocolatey](http://chocolatey.org), my favorite Package Manager for that OS, to easily install Python and any kind of free software you like (or mostly any, since the chocolatey package repository is pretty large!).

Now, let's install the Pelican, Markdown and ghp-import Python modules:

```
$ pip install pelican markdown ghp-import
```

In addition to Pelican:

- [Markdown](http://whatismarkdown.com) is a popular lightweight markup languages well suited for web content
- [ghp-import](https://github.com/davisp/ghp-import) will be used later to publish the blog to the target GitHub Page

Let's configure Pelican:

```bash
$ mkdir MyBlog
$ cd MyBlog
$ pelican-quickstart
```

Basically, you can keep all the default parameters, except of course for:

- Title of the Web site: choose your title
- Author of the Web site: put your name or pseudo depending on your preferences
- URL prefix: answer 'Y' and specify the GitHUb User page URL 'http://*github-user-name*.github.io/'

As a result, the `MyBlog` directory now contains the Pelican default file tree.

The [Pelican documentation](http://docs.getpelican.com) will give you more insights on all possible parameters.

### Create a first Article & locally Preview your Blog
All you have to do, is to go to the `content` directory in the hierarchy create in the previous paragraph, and create the file that will contain your first Post.

You can name the file as you want, e.g. `My-1st-post.md`.

File content format is:

* the header, with the following lines: 'Title: _Post title_', 'Date: _Post date_', 'Category: _Post category_' and 'Tags: _list of coma separated Post tags_',
* the content, written by default in reStructuredText (aka rst) or in Markdown markup languages.

I prefer using Markdown rather than Pelican's default rst, that's why I added mardown module to the `pip install` command detailed earlier in this article.

Here is an example article file in Markdown, borrowed from the Pelican documentation:
```markdown
Title: My first review
Date: 2010-12-03 10:20
Category: Review

# Product of the Year Review!
This is an **Awesome** product
```

You might find GitHub's [Markdown Guide](https://guides.github.com/features/mastering-markdown) helpful.

Now, from the project main directory, run pelican to generate the static html content and then launch a local webserver:
```
$ pelican content
$ python -m pelican.server
```
Alternatively, there's another possible way to launch the local webserver by using the pelican provided script:
```
$ ./development_server.sh start
```
(but in my case, on Windows and from GitBash, I had to create a symlink from `python.exe` to `python3.exe` to make it work)

Now, check the result by opening a browser at [http://localhost:8000](http://localhost:8000)

### Install & Setup a Theme (Optional)
Now we have a first start for the content, it's time to work on the presentation.
It's of course possible to design your very own presentation by developing  
Pelican has a fair amount of themes you can discover & dowload [here](http://www.pelicanthemes.com).
I choose `pelican-blue` and cloned it from the project's GitHub [repository](https://github.com/Parbhat/pelican-blue).

For this, I'd recommend creating a `pelican-themes` directory in your pelican project dir:
```
mkdir pelican-themes
cd pelican-themes
git clone https://github.com/Parbhat/pelican-blue.git
```
Then, import the theme into your Pelican config:
```
cd ..
pelican-themes -i pelican-themes/pelican-blue
```
No sure for each theme you might like & use, but in my case, the GitHUb repo `Readme.md` file described variables to be setup in the `pelicanconf.py` file:
```
THEME = 'path-to-pelican-blue-theme'
SIDEBAR_DIGEST = 'Programmer and Web Developer'
FAVICON = 'url-to-favicon'
DISPLAY_PAGES_ON_MENU = True
TWITTER_USERNAME = 'twitter-user-name'
MENUITEMS = (('Blog', SITEURL),)
```
In my own setup, I also discovered a non-documented variable `PAGES = True` required to have static pages appearing in my Blog Menu (in addition to having a `pages` subdirectory in the `content` directory). But that may be related to the way the specific way the `pelican-blue` theme is developed.

### Publish your local Blog copy to your GitHub repository

During the 1st step, we've created the GitHub repository for the User page.

Since then, we've generated and tested some content locally.

So now, we want to upload our content, I mean the files in the `output` directory of your project to the `master` branch of your GitHub User page repository, which is the branch that will be accessible through the `https://**username**.github.io` URL.


