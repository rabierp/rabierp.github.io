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

I prefer using Markdown rather than Pelican's default rst, that's why I added mardown module to the `pip install` command detailed earlier in this article.

You can name the file as you want, e.g. `My-1st-post.md`.
File content format is:

* the header, with the following lines: 'Title: _Post title_', 'Date: _Post date_', 'Category: _Post category_' and 'Tags: _list of coma separated Post tags_':
  ** 1
  ** 2
* the content, written by default in reStructuredText (aka rst) or in Markdown markup languages.


Here is an example article file in Markdown, borrowed from the Pelican documentation:
```markdown
Title: My first review
Date: 2010-12-03 10:20
Category: Review

# Product of the Year Review!
This is an **Awesome** product
```

You might find Adam Pritchard's [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) helpful.

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

### Publish your local Blog copy to your GitHub repository


