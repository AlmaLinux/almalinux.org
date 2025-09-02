# Contributing - Blog Posts

adding crap to see if prettier fixes it
_do not merge this_
still bad

We welcome blog posts of almost any kind from our community! We accept content that covers topics that relate to AlmaLinux OS, the AlmaLinux OS Foundation. If you aren't sure if your blog post topic would be a good one, feel free to create an issue on this repo and ask! You can also join our chat and ask in the Marketing room.

### Process

- Before you begin writing the blog post, we strongly recommend that you search existing open and closed issues [and existing blog posts](https://github.com/AlmaLinux/almalinux.org/tree/master/content/blog) for similar content, to prevent duplication.
- We also recommend that you open an issue on the repo to propose your blog post before you begin writing it, to ensure that your blog post would be appropriate for the AlmaLinux blog.
- Please fork the [almalinux.org](https://github.com/AlmaLinux/almalinux.org) repo and submit a pull request with your blog post addition from there.
- Once you submit your pull request, tag @bennyvasquez for a review.

#### The content of your .md file

Our website is built in Hugo and served using CloudFlare pages, so you may find some quirks. To add a blog post successfully to the website, take the steps below, and reach out in [~marketing](https://chat.almalinux.org/almalinux/channels/marketing) on our chat server if you have any problems.

**The blog file**

Blog content is served using the `layouts/blog/single.html` format. Note: if you would like to suggest changes to this format, they should be submitted in a PR outside the PR of your blog post.

- create a new file in `./content/blog` named what you'd like the slug (URL) to be, with a file extension of '.md'. For example, the blog post at [almalinux.org/blog/celebrating-500k-docker-pulls](almalinux.org/blog/celebrating-500k-docker-pulls) is in a file named `./content/blog/celebrating-500k-docker-pulls.md`.

**The Meta data**

- The top of your file should be the metadata for your post. The meta information should be updated to include your posts information. The content is defined and further explained below.

```
---
title: ""
type: blog
author:
 name: ""
 bio: ""
 image: /users/
date: ''
images:
  - /blog-images/
post:
	title: ""
	image: /blog-images/
---
```

- The **title** is what you'd like displayed at the top of the post.
- The **type** should always be blog.
- The **name** listed should be yours (either legal name or chosen name or moniker)
- Your **bio** will be displayed directly under your name, so please keep this to 60 characters or less. If you would like to leave this blank, you may do so.
- Your author **image** should be appropriate for an all-audiences website and added to `./static/users/` in .png format. The file will serve from `/users/`, so do not change the beginning of this path.
- The **date** is the date (in YYYY-MM-DD format) you want to see the blog post published, but we cannot always guarantee a publishing timeline.
- The **images** image is the social image that's used, and should be put in `./static/blog-images/`
- The post **title** should match the above.
- A post **image** should be included, and will be displayed both on the [almalinux.org/blog/](almalinux.org/blog/) feed, and as the header image on the full-page blog post. Use this tempalte to get started: `./static/blog-images/blog_images_template.svg`
  - Your image should not violate any trademarks or copyrights, and should be relevant to blog content. Once created, a PNG version of your image should be placed in `./static/blog-images/` The file will serve from `/blog-images/`, so do not change the beginning of this path.

**The meat of your post**

- Below the --- of the metadata block, you should place the content of your blog post. This content should be in markdown format, and any images you want to include in your post can be added to `./static/blog-images/` and will serve from `/blog-images/`.
- Using the '[figure](https://gohugo.io/content-management/shortcodes/#figure)' short code for images can give you more control in how they're displayed. For example:
  `{{< figure src="/images/certificationimages/certificationprocess.svg" link="/images/certificationimages/certificationprocess.svg" caption="The Hardware Certification Process" width="100%">}}`
- Before submitting your PR, please test that your content loads correctly by building the site locally with the command `hugo server`
- Adding YouTube embeds:\
  To embed YouTube videos we suggest you use the [YouTube shortcode](https://gohugo.io/content-management/shortcodes/#youtube) supplied by Hugo and modified by our contributors to include height and width customization with better mobile support, here is an overview of how to use it:
  - **YouTube ID** - The youtube ID can be allocated from the video link, for example in this video `https://www.youtube.com/watch?v=dQw4w9WgXcQ`, the ID is `dQw4w9WgXcQ`. (the value of "v" is the video ID)
  - `allowFullScreen=true` - Whether the video can activate full screen mode.
  - `autoplay=false` - Whether to automatically play the video. Forces mute to be true.
  - `class` - The class attribute of the wrapping div element. Specifying removes style attributes from the iframe and its wrapping div.
  - `controls=true` - Whether to display the video controls.
  - `end` - The time, in seconds from the video start, when the player should stop playing.
  - `id` - The video id. Optional if provided as the first positional argument.
  - `loading=eager` - The loading attribute of the iframe.
  - `loop=false` - Whether to indefinitely repeat the video. Ignores start and end after the first play.
  - `mute=false` - Whether to mute the video. Always true when autoplay is true.
  - `start` - The time, in seconds from the video start, when the player should start playing.
  - `title` - The title attribute of the iframe element. Defaults to "YouTube video".
  - `width` - The width of the video, specified in px, %, vw, em, rem, cm, in, mm, pt, or pc.
  - `height` - The height of the video, specified in px, %, vh, em, rem, cm, in, mm, pt, or pc.

  For example:

  ```html
  {{< youtube id="Video ID" width="45%" height="25%" autoplay="false"
  controls="true" mute="false" title="I love AlmaLinux" >}}
  ```

### Some notes about content

- define all terms used (especially acronyms) so that all readers may understand your content.
- content submitted to the AlmaLinux blog should be unique and not posted elsewhere on the internet.
- by submitting content to the AlmaLinux website, you acknowledge that you are aware of our [license policy](https://almalinux.org/p/the-almalinux-os-licensing-policy/), are affirming that you own all rights to publish said content.
- external links are allowed, but links to paywalled websites or obvious use of a blog post on the AlmaLinux site as an SEO builder for another website is prohibited. By default, external links should include a '[nofollow](https://en.wikipedia.org/wiki/Nofollow)' value. Exceptions can be requested in your pull request.

### Styling Guide

Please adhere to the styling guidelines listed below when contributing to the codebase.

#### Code/Syntax Highlighting

Code/Syntax highlighting is achieved by the builtin [Hugo syntax highlighting](https://gohugo.io/content-management/syntax-highlighting/) feature, which utilizes [Chroma](https://github.com/alecthomas/chroma).

While Hugo supports two syntaxes, we use traditional code fencing for code samples:

````plaintext
```go
package main

import "fmt"

func main () {
    fmt.Println("AlmaLinux is neat-o!")
}
```
````

Supported highlighting languages can be found [here](https://gohugo.io/content-management/syntax-highlighting/#list-of-chroma-highlighting-languages).
