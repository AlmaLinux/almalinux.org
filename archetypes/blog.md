{{- $year := now | dateFormat "2006" -}}
{{- $date := now | dateFormat "2006-01-02" -}}
---
title: "{{ replace (replaceRE `^\d{4}-\d{2}-\d{2}-` "" .Name) "-" " " | title }}"
type: blog
author:
  name: "Your Name"
  bio: "Your Title or Role"
  image: /users/username.jpg
date: {{ $date }}
images:
  - /blog-images/{{ $year }}/image-name.png
post:
  title: "A one- or two-sentence summary of the post, shown on the blog listing page"
  image: /blog-images/{{ $year }}/image-name.png
---

Opening paragraph summarizing the post.

## Section heading

Content here.

{{ "{{<" }} figure src="/blog-images/{{ $year }}/image-name.png" width="50%" class="text-center" >}}
