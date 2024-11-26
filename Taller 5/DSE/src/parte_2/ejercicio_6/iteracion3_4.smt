(declare-const k Real)
;c1_0
(assert (and (< 0 3) (>= 0 0)))
;c2_0
(assert (=(+ k 5.0) 0))
(check-sat)
(get-model)