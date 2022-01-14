# Graph Design Rules

<details>

## Table of Contents  
- Types of Graphs  
- Filter
- Packages  

</details>

---
## Types of Graphs

### Crosstable  


### Histogramm  
single measure. heigth is number of observations that fit in a given range / bin

### Boxplot  
variability and extreme values of a measure
range, max , min, std, mean, median

### Barchart  
compare aggregate data. compare nominal values, time series, of 100% bar chart. part of whole
normal, stacked, stacked 100%, // same 90 degrees rotated

### Geomap  
coordinates, dot density map // region maps // bubbles with size and color // contour map

### treemap  
compare two measures

### radar chart  

### area  
normal, stacked, stacked 100%

### plane  
normal, drahtmodell-- only contours

### sunburst  


### waterfall  


### relationship plot  
corr plot, scatter plot (plot trend line or regression), heat map

### fit line  
linear, quadratic, cupe PSline

### bubble plot  
horizobtal, vertical, size bubble, color, (animate)

### time plot  
line chart, time series plot, (connectrs data values) show trend measure.
linechart: normal, stacked, stacked 100%, with dots ..


### forecast chart  
with confident interval. define period
hindcast values, historical values...
ARIMA, damped trend expon smoothing, linear exp. smoothing. winters method, seasonal smoothing, simple smoothing

### piecharts  
vary greatly

### donut chart  
better, more instinct

### wordcloud  
text


### vector plot  
quiver plot

### butterflychart  


### needle plot  


### dot plot
between categorical, like bar chart

### flowchart  
path chart

### dual axis charts  
bar, bar/line, line, time series
- shared category axis on xaxis. only if does not depend on prior value
- bar line: line shows trend.. is dependend on prior. bar is always un dependent
- line: depents on prior


---
## Display Rules
expression display rules: backround of graph, graph itself
color map value: dependend on category value!
table: indivindual numbers, ampel, category, cutoff value, gauge
arrows and names. value ontop, format


---
## Filter
- drop down
- list
- button
- text
- slider


---
## Packages  
- altair
- bokeh
- cartopy
- pandas
- plotly
- matplotlib
- scikit
- seaborne
- geoplotlib
- ggplot
- yellowbrick
