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

# Known issues
Works only on mac os. To make it work on linux and windows need to use another method to get file's creation date. See references (1)

# References
1. https://stackoverflow.com/questions/237079/how-to-get-file-creation-modification-date-times
2. https://stackoverflow.com/questions/5914627/prepend-line-to-beginning-of-a-file
3. https://careerkarma.com/blog/python-list-files-in-directory/
4. https://stackoverflow.com/questions/55406067/filtering-os-walk-files-on-extension-and-size