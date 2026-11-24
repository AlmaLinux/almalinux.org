{{- /*
  Expects a file name like 2026-11-11-almalinux-news-november-2026.md
  (publish date, then the issue's month spelled out and its year).
  Run: npx hugo new newsletters/2026-11-11-almalinux-news-november-2026.md
*/ -}}
{{- $parts := split .File.ContentBaseName "-" -}}
{{- if eq (len $parts) 7 -}}
{{- $month := index $parts 5 -}}
{{- $year := index $parts 6 -}}
---
title: "AlmaLinux News for {{ title $month }} '{{ substr $year 2 2 }}"
type: newsletters
date: "{{ delimit (first 3 $parts) "-" }}"
summary: ""
image: /newsletter-images/{{ substr $month 0 3 }}-{{ substr $year 2 2 }}.png
draft: false
---
{{- else -}}
---
title: "AlmaLinux News for Month 'YY"
type: newsletters
date: "{{ now | dateFormat "2006-01-02" }}"
summary: ""
image: /newsletter-images/mon-yy.png
draft: false
---
{{- end }}
