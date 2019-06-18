(define (problem probLOGISTICS-5-0) (:domain logistics)
(:objects
	obj21 - package
	obj22 - package
	obj23 - package
	apt2 - airport
	apt1 - airport
	obj11 - package
	obj13 - package
	obj12 - package
	pos2 - location
	cit1 - city

	(:private
		tru1 - truck
		pos1 - location
	)
)
(:init
	(at tru1 pos1)
	(at obj11 pos1)
	(at obj12 pos1)
	(at obj13 pos1)
	(at obj21 pos2)
	(at obj22 pos2)
	(at obj23 pos2)
	(in-city tru1 pos1 cit1)
	(in-city tru1 apt1 cit1)
)
(:goal
	(and
		(at obj23 apt2)
		(at obj22 apt1)
		(at obj13 apt2)
		(at obj12 pos2)
		(at obj11 pos2)
	)
)
)
