(declare-const k Real)
;c1_0
(assert (and (< 0 3) (>= 0 0)))
; not c2_0
(assert (not(=(+ k 5.0) 0)))
;not c1_1
(assert (not(and (< 1 3) (>= 1 0))))

(check-sat)
(get-model)