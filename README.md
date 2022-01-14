# About
A small script that create frontmatter in .md files in given directory based on their creation and last modified dates.

### Before
example.md
``` 
Some content here
## blah blah blah
```

### After
example.md
``` 
---
created: 2021-10-06T18:57:10+03:00
updated: 2021-10-18T13:56:26+03:00
---
Some content here
## blah blah blah
```

# References
https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times
https://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
https://careerkarma.com/blog/python-list-files-in-directory/
https://stackoverflow.com/questions/55406067/filtering-os-walk-files-on-extension-and-size
