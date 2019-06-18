(define (problem probLOGISTICS-14-0) (:domain logistics)
(:objects
	obj41 - package
	apt3 - airport
	apt2 - airport
	apt1 - airport
	apt5 - airport
	apt4 - airport
	pos4 - location
	pos5 - location
	pos2 - location
	pos3 - location
	obj21 - package
	obj22 - package
	obj23 - package
	obj33 - package
	obj32 - package
	obj31 - package
	obj42 - package
	obj43 - package
	obj53 - package
	obj52 - package
	obj11 - package
	obj51 - package
	obj13 - package
	obj12 - package
	tru3 - truck
	cit3 - city
	cit4 - city
	tru4 - truck
	cit2 - city
	tru2 - truck
	apn1 - airplane

	(:private
		tru5 - truck
		cit5 - city
	)
)
(:init
	(at obj21 pos2)
	(at obj22 pos2)
	(at obj23 pos2)
	(at obj31 pos3)
	(at obj32 pos3)
	(at obj33 pos3)
	(at obj41 pos4)
	(at obj42 pos4)
	(at obj43 pos4)
	(at tru5 pos5)
	(at obj51 pos5)
	(at obj52 pos5)
	(at obj53 pos5)
	(in-city tru5 pos5 cit5)
	(in-city tru5 apt5 cit5)
	(at tru3 pos3)
	(in-city tru3 pos3 cit3)
	(in-city tru3 apt3 cit3)
	(at tru4 pos4)
	(in-city tru4 pos4 cit4)
	(in-city tru4 apt4 cit4)
	(at tru2 pos2)
	(in-city tru2 pos2 cit2)
	(in-city tru2 apt2 cit2)
	(at apn1 apt2)
)
(:goal
	(and
		(at obj51 apt5)
		(at obj53 apt5)
		(at obj23 pos2)
		(at obj31 pos5)
		(at obj12 apt3)
		(at obj32 pos4)
		(at obj13 apt1)
		(at obj42 pos4)
		(at obj41 apt3)
		(at obj11 apt4)
		(at obj22 pos4)
		(at obj43 apt5)
		(at obj33 pos3)
		(at obj21 pos5)
	)
)
)