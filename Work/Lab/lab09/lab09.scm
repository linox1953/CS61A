(define (over-or-under num1 num2) 
  (cond ((> (- num1 num2) 0) 1)
        ((< (- num1 num2) 0) -1)
        ((= (- num1 num2) 0) 0)
  )
)

(define (make-adder num) 
  (lambda (inc) (+ num inc))
)

(define (composed f g) 
  (lambda (x) (f (g x)))
)

(define (repeat f n) ; How to do this? I can't do this
  ; IMPORTANT It's a little difficult to understand
  (if (= n 0)
      (lambda (x) x)
      (composed f (repeat f (- n 1))))
)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (if (zero? (modulo a b))
      b
      (gcd b (modulo a b)))
)
