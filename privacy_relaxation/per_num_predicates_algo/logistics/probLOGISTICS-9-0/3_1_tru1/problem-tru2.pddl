(define (problem probLOGISTICS-9-0) (:domain logistics)
(:objects
	obj21 - package
	obj22 - package
	obj23 - package
	obj33 - package
	obj32 - package
	obj31 - package
	apt3 - airport
	apt2 - airport
	apt1 - airport
	obj11 - package
	obj13 - package
	obj12 - package
	pos3 - location
	pos1 - location
	pos2 - location
	apn1 - airplane
	tru1 - truck

	(:private
		cit2 - city
		tru2 - truck
	)
)
(:init
	(at obj11 pos1)
	(at obj12 pos1)
	(at obj13 pos1)
	(at tru2 pos2)
	(at obj21 pos2)
	(at obj22 pos2)
	(at obj23 pos2)
	(at obj31 pos3)
	(at obj32 pos3)
	(at obj33 pos3)
	(in-city tru2 pos2 cit2)
	(in-city tru2 apt2 cit2)
	(at apn1 apt2)
	(at tru1 pos1)
)
(:goal
	(and
		(at obj23 pos3)
		(at obj32 pos1)
		(at obj22 pos1)
		(at obj31 apt3)
		(at obj11 pos1)
		(at obj33 pos3)
		(at obj13 apt3)
		(at obj12 pos1)
		(at obj21 apt1)
	)
)
)
