---
title: "Wymore - Resources"
layout: textlay
excerpt: "Wymore at the University of Michigan, Ann Arbor."
sitemap: false
permalink: /resources/
---

# Resources

Here are some resources you might find useful.

## Scripts

Here are some scripts we built. Use and modify as you want.

Please, include a citation.

### Clustering

This script will filter out sequences from a fasta file that are not in a certain sequence length range. The Python script take an input fasta file name (this is the file with sequences), the output file name, the min length, and the max length. You can include a --visual flag at the end to have matplotlib create a histogram of the sequence lengths.

You can download the script [here]({{ site.url }}{{ site.baseurl }}/scripts/ClusterByLengthMargin.py)

### Gather Sequence Information

This script parses a fasta file and downloads information from online databases. The information is then put into an excel spreadsheet. This script may require some editting and adjusting for your use.

You can download the script [here]({{ site.url }}{{ site.baseurl }}/scripts/get_info.py)

### Reorder Sequence Information

This script allows you to reorder the information from an excel spreadsheet to the order of another fasta file. This is useful for reordering sequences after sorting according to a phylogenetic tree.

You can download the script [here]({{ site.url }}{{ site.baseurl }}/scripts/reorder_metadata.py)
