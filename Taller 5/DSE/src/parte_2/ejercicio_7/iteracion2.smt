(declare-const n Int)
;c1_0
(assert (< 0 n))
;c1_1
(assert (< 1 n))
(check-sat)
(get-model)