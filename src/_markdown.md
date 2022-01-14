# Markdown Cheatsheet

<details>
<summary>Table of contents</summary>

## Table of contents
* [Headers](#headers)
* [Emphasis](#emphasis)
* [Horizontal Lines](#horizontal-lines)
* [Blockquotes](#blockquotes)
* [Lists](#lists)
* [Tables](#tables)
* [Code](#code)
* [Syntax Highlights](#syntax-highlights)
* [Anchors and References](#anchors-and-references)
* [HTML](#html-syntax)
* [Badges](#badges)
* [Emojis](#emojis)

</details>

---
## Headers
_Code_
```
# H1
## H2
### H3
#### H4
##### H5
###### H6
```

_Examples_
# H1
## H2
### H3
#### H4
##### H5
###### H6

---
## Emphasis
_Code_
```
_italic_ or *italic*  
__bold__ or **bold**  
__bold and *italic*__  
~~Striked~~  
```

_Examples_
_italic_ or *italic*  
__bold__ or **bold**  
__bold and *italic*__  
~~Striked~~  

---
## Horizontal Lines
_Code_
```
---
***
___

```

_Examples_
---  
***  
___  

---
## Blockquotes
_Code_
```
> Ongoing quote  
> from a philosopher  
>> Level 2  
>>> Level 3  
```

_Examples_
> Ongoing quote
> from a philosopher
>> Level 2
>>> Level 3

---
## Lists
_Code_
```
Ordered list
1. Item 1
2. Item 2
3. Item 3

Unordered list
* Item 1
* Item 2
* Item 3

- Item 1
- Item 2
- Item 3

Nested list
* Item 1
  * Item 2
    Explanation indents
     * Item 3

```

_Examples_
### Ordered list
1. Item 1
2. Item 2
3. Item 3

### Unordered list
* Item 1
* Item 2
* Item 3

_or_
- Item 1
- Item 2
- Item 3

### Nested Lists
* Item 1
  * Item 2
     * Item 3

### Tasks
_Code_
```
- [ ] Uncompleted
- [x] Completed
```

_Examples_
- [ ] Uncompleted
- [x] Completed

---
## Tables
_Code_
```
Basic table
| Column Header | Column Header |
| ------------- | ------------- |
| Row 1         | Row 1         |
| Row 2         | Row 2         |

Aligned table
| Column Header | Column Header | Column Header |
| :---          |     :----:    |          ---: |
| Row 1         | Row 1         | Row 1         |
| Row 2         | Row 2         | Row 2         |

```

_Examples_

| Column Header | Column Header |
| ------------- | ------------- |
| Row 1         | Row 1         |
| Row 2         | Row 2         |

| Column Header | Column Header | Column Header |
| :---          |     :----:    |          ---: |
| Row 1         | Row 1         | Row 1         |
| Row 2         | Row 2         | Row 2         |


---
## Code
_Code_
````
Inline higlight:  
`Piece of code`  

Codeblocks:  
~~~
Piece of code using ~  
~~~
```
Piece of code using `  
```
````

_Examples_
Inline higlight:  
`Piece of code`  

Codeblocks:  
~~~
Piece of code using ~  
~~~
```
Piece of code using `  
```

---
## Syntax Highlights
~~~
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
~~~

_Examples_
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```

_some supported languages_:  
c, css, csv, http, java, javascript, json, markdown, python, sql, xml, yaml  

[Reference](http://www.rubycoloredglasses.com/2013/04/languages-supported-by-github-flavored-markdown/)  

---
## Anchors and References
_Code_
```
[Anchor](#anchor)  
[Reference using link](https://www.google.com)  
[Reference using number][1]  
[Reference using text][text reference]  
<https://www.google.com>   
[1]: https://www.google.com  
[text reference]: https://www.google.com  
```

_Examples_  
[Anchor](#anchor)  
[Reference using link](https://www.google.com "google.com")  
[Reference using number][1]  
[Reference using text][text reference]  
<https://www.google.com>   

[1]: https://www.google.com  
[text reference]: https://www.google.com  

---
## HTML Syntax

### Headings
_Code_  
```
<h4>Heading level 1</h4>
```

_Example_  
<h4>Heading level 1</h4>

### Emphasis
_Code_  
```
This is <strong>bold</strong> and this is <em>italic</em>.
```

_Example_  
This is <strong>bold</strong> and this is <em>italic</em>.

### Lists
#### Ordered List
_Code_  
```
<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
<li>Fourth item</li>
</ol>
```

_Example_  
<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
<li>Fourth item</li>
</ol>

#### Unordered List
_Code_  
```
<ul>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
<li>Fourth item</li>
</ul>
```

_Example_  
<ul>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
<li>Fourth item</li>
</ul>

### Tables
_Code_  
```
<table>
    <tr>
        <td>Table Data</td>
        <td>Table Data</td>
    </tr>
</table>
```

_Example_  
<table>
    <tr>
        <td>Table Data</td>
        <td>Table Data</td>
    </tr>
</table>

### Code
_Code_  
```
At the command prompt, type <code>nano</code>.
```

_Example_  
At the command prompt, type <code>nano</code>.

### Anchors and References
_Code_  
```
<h4 name="setup">Setup</h4>  
<p>
  <a href="https://google.com">google.com</a>
</p>
```

_Example_  
<h4 name="setup">Setup</h4>  
<p>
  <a href="https://google.com">google.com</a>
</p>

### Miscancellous
&nbsp; indent  
Line</br>break 

---
## Emojis

:relaxed: `:relaxed:`
:wink: `:wink:`
:smile: `:smile:`
:smiley: `:smiley:`
:flushed: `:flushed:`
:stuck_out_tongue_winking_eye: `:stuck_out_tongue_winking_eye:`
:sleeping: `:sleeping:`
:worried: `:worried:`
:confused: `:confused`
:unamused: `:unamused:`
:joy: `:joy:`
:+1: `:+1:`
:-1: `:.1:`
:raised_hand: `:raised_hand:`
:point_left: `:point_left:`
:point_rigt: `:point_rigt:`
:point_up: `:point_up:`
:muscle: `:muscle:`
:zap: `:zap:`
:copyright: `:copyright:`
:registered: `:registered:`
:tm: `:tm:`
:x: `:x:`
:heavy_exclamation_mark: `:heavy_exclamation_mark:`
:heavy_multiplication_x: `:heavy_multiplication_x:`
:heavy_plus_sign: `:heavy_plus_sign:`
:heavy_minus_sign: `:heavy_minus_sign:`
:heavy_division_sign: `:heavy_division_sign:`
:heavy_check_mark: `:heavy_check_mark:`  

[Reference](https://gist.github.com/rxaviers/7360908)

---
## Badges
[![Generic Badge](https://img.shields.io/badge/badge-works!-brightgreen)](https://shields.io/)
[![Repo Size](https://img.shields.io/github/size/JanAlexanderZak/cheatsheets/markdown.md)](https://shields.io/)
[![Repo Size](https://img.shields.io/github/size/JanAlexanderZak/cheatsheets/markdown.md)]

---
## Escape Characters
**\\** infront of:
* \
* `
* \*
* _
* {}
* []
* ()
* \#
* \+
* \-
* .
* !
