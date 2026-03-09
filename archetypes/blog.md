{{- $year := now | dateFormat "2006" -}}
{{- $date := now | dateFormat "2006-01-02" -}}

---

title: "{{ replace .Name "-" " " | title }}"
type: blog
author:
name: "Your Name"
bio: "Your Title or Role"
image: /users/username.jpg
date: {{ $date }}
images:

- /blog-images/{{ $year }}/image-name.png
  post:
  title: "{{ replace .Name "-" " " | title }}"
  image: /blog-images/{{ $year }}/image-name.png

---

Opening paragraph summarizing the post.

## Section Heading

Content here.

{{</* figure src="/blog-images/{{ $year }}/image-name.png" width="50%" class="text-center" \*/>}}
