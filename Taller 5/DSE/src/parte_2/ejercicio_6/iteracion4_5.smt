(declare-const k Real)
;not c1_0
(assert (not(and (< 0 3) (>= 0 0))))
(check-sat)
(get-model)