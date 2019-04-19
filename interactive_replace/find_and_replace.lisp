;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; What does this script do?
; Interactively iterate over all files with extension *file_extension*, looking for the string
; *find_string* and replace it with *replace_with*, asking the user for permission to do so everytime.
; Ref: http://ergoemacs.org/emacs/find_replace_inter.html

; How to use this script?
; 1. Keep this file in the directory where you want the replacements to take place
; 2. Open this file in emacs.
; 3. With this file open in a buffer, use the command (M-x eval-buffer). Give 'y' or 'n' prompt to do the replacements.

; Warning
; If the updates in this code doesn't take effect, restart emacs.

; TODO
; * Add support to search in sub-directories.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;(defun find_and_replace()

; Customize this scrip here
(setq *file_extension* "\.v$")
(setq *find_string* "hi")
(setq *replace_with* "omg")

(message "Interactive find and replace of strings")
(message "My first emacs lisp")
(dired default-directory)
;(dired-unmark-all-files) ; TODO
(dired-mark-files-regexp *file_extension*)
(dired-do-query-replace-regexp *find_string* *replace_with*)
;)

;(find_and_replace())
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Save the files which are open in Emacs, manually.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; Method 1 (Preferred)
; (C-u C-x s)

; Method 2
;(ibuffer)
;(*u)
;(S)
;(D)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
