(declare-const n Int)
;c1_0
(assert (< 0 n))
(check-sat)
(get-model)