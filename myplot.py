#!/usr/bin/env python


import matplotlib.pyplot as plt

# http://www.randalolson.com/2014/06/28/how-to-make-beautiful-data-visualizations-in-python-with-matplotlib/
pretty_colors = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120), (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150), (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148), (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199), (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]
for i in range(len(pretty_colors)):  
    r, g, b = pretty_colors[i]  
    pretty_colors[i] = (r / 255., g / 255., b / 255.)  

# Pie chart
def plot_pie(data, labels, img_name, legendOn = False):
  fig, ax = plt.subplots()
  # for text in autotexts:
  #   text.set_fontsize(14)
  # for text in texts:
  #   text.set_fontsize(14)
  if (legendOn):
    patches, texts, autotexts = ax.pie(data, autopct='%1.1f%%', colors=pretty_colors)
    indices = [x.split()[-1] for x in labels]
    ax.legend(patches, indices,
          title="Individuals",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
  else:
    patches, texts, autotexts = ax.pie(data, labels = labels, autopct='%1.1f%%', colors=pretty_colors)
    plt.setp(texts, size=14, weight="bold")
  plt.setp(autotexts, size=14, weight="bold")
  plt.savefig('figures/' + img_name + '.pdf',  bbox_inches = 'tight',
    pad_inches = 0)
  plt.close(fig) # close the figure
  return