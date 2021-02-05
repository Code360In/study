CREATE TABLE presidents (
  country                 VARCHAR   PRIMARY KEY,
  continent               VARCHAR,
  president               VARCHAR
);

CREATE TABLE prime_ministers (
  country                 VARCHAR   PRIMARY KEY,
  continent               VARCHAR,
  prime_minister          VARCHAR
);

CREATE TABLE states (
  name                    VARCHAR   PRIMARY KEY,
  continent               VARCHAR,
  indep_year              INTEGER,
  fert_rate               REAL,
  women_parli_perc        REAL
  
);

CREATE TABLE monarchs (
  country                 VARCHAR   PRIMARY KEY,
  continent               VARCHAR,
  monarch                 VARCHAR
);

select *
from presidents;

select *
from prime_ministers;

#inner join
select p1.country, p1.continent,
	p1.prime_minister, p2.president
from prime_ministers as p1
inner join presidents as p2
on p1.country = p2.country;

select p1.country, p1.continent,
	p1.prime_minister, p2.president
from prime_ministers as p1
inner join presidents as p2
using (country);

select p1.country as country1, p2.country as country2, p1.continent
from prime_ministers as p1
inner join presidents as p2
on p1.continent = p2.continent
limit 14;

select p1.country as country1, p2.country as country2, p1.continent
from prime_ministers as p1
inner join presidents as p2
on p1.continent = p2.continent and p1.country <> p2.country
limit 14;

select *
from states;

select name, continent, indep_year,
	case when indep_year < 1900 then 'before 1900'
		 when indep_year <= 1930 then 'between 1900 and 1930'
		 else 'after 1930' end
		 as indep_year_group
from states
order by indep_year_group

#left join
select p1.country, p1.prime_minister, p2.president
from prime_ministers as p1
left join presidents as p2
on p1.country = p2.country;

# full join 
select p1.country as pm_co, p2.country as pres_co,
	 p1.prime_minister, p2.president
from prime_ministers as p1
full join presidents as p2
on p1.country = p2.country;

#cross join
select p1.prime_minister, p2.president
from prime_ministers as p1
cross join presidents as p2
where p1.continent in ('North America', 'Oceania');

select *
from monarchs;

#union - 중복제거
select prime_minister as leader, country
from prime_ministers
union
select monarch, country
from monarchs
order by country;

#union all
select prime_minister as leader, country
from prime_ministers
union all
select monarch, country
from monarchs
order by country
limit 10;

#intersect
select country
from prime_ministers
intersect
select country
from presidents;

select country, prime_minister as leader
from prime_ministers
intersect
select country, president
from presidents;

#Except
select monarch, country
from monarchs
except
select prime_minister, country
from prime_ministers;

#semi-join
select name
from states
where indep_year < 1800;

select president, country, continent
from presidents;

select president, country, continent
from presidents
where country in
	(select name
	from states
	where indep_year < 1800);
	
#anti-join
select president, country, continent
from presidents
where continent like '%America'
	and country not in
		(select name 
		from states
		where indep_year < 1800);

select avg(fert_rate)
from states;

select name, fert_rate
from states
where continent = 'Asia'

select name, fert_rate
from states
where continent = 'Asia'
	and fert_rate <
		(select avg(fert_rate)
		 from states);

select DISTINCT continent,
	(select COUNT(*)
	from states
	where prime_ministers.continent = states.continent) as countris_num
from prime_ministers;

select continent, max(women_parli_perc) as max_perc
from states
group by continent
order by continent;

select monarchs.continent
from monarchs, states
where monarchs.continent = states.continent
order by continent;

select distinct monarchs.continent, subquery.max_perc
from monarchs,
	(select continent, max(women_parli_perc) as max_perc
	 from states
	 group by continent) as subquery
where monarchs.continent = subquery.continent
order by continent;
