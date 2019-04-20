Interactivley do find and replace of certain strings in files with pre-set extensions.

### Updates
* xah-find-replace works, but not in interactive mode. Also you need to use Emacs25 (not Emas24) to make it work. [Ref](http://ergoemacs.org/emacs/elisp-xah-find-text.html). The workaround is to do the replacements in non-interactive mode and analyze the *xah-find output* buffer in Emacs for the results of replacements, visit each of those files separately and undo the replacement manually, whereever required.

Note: 
  interactive_replace.py doesn't work
