# Simple Grammar for Chinese

## MySplitter
```console
python3 MySplitter.py dictionary.utf-8 sentence.utf-8 result.utf-8
```
* `dictionary.utf-8` is the file defining a dictionary of words
* `sentence.utf-8` is the file for sentences to be splitted
* `result.utf-8` is the file for the output of the splitted words

## MyCharty
```console
python3 MyCharty.py -g PSG3.txt -i result.utf-8
```
* `PSG3.txt` is the file for the grammar
* `result.utf-8` is the file containing the splitted sentence which will be analysed