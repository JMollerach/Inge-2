(declare-const k Real)
;c1_0
(assert (and (< 0 3) (>= 0 0)))
; not c2_0
(assert (not(=(+ k 5.0) 0)))
;c1_1
(assert (and (< 1 3) (>= 1 0)))
;not c2_1
(assert (not(=(+ k 1.0) 0)))
;c1_2
(assert (and (< 2 3) (>= 2 0)))
;not c2_2
(assert (not(=(+ k 3.0) 0)))
;c1_3
(assert (and (< 3 3) (>= 3 0)))
(check-sat)
(get-model)