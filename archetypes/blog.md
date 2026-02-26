---
title: "{{ replace .Name "-" " " | title }}"
type: blog
author:
  name: "Your Name"
  bio: "Your Title or Role"
  image: /users/username.jpg
date: "{{ .Date.Format "2006-01-02" }}"
images:
  - /blog-images/{{ .Date.Format "2006" }}/image-name.png
post:
  title: "{{ replace .Name "-" " " | title }}"
  image: /blog-images/{{ .Date.Format "2006" }}/image-name.png
---

Opening paragraph summarizing the post.

## Section Heading

Content here.

{{</* figure src="/blog-images/{{ .Date.Format "2006" }}/image-name.png" width="50%" class="text-center" */>}}
