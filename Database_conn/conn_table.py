from faker import Faker
import sqlite3

conn = sqlite3.connect('employee.db')

fk = Faker()

# create table query -->
query = 'create table emp(emp_id number, name char, salary number, phone char, email char)'
# conn.execute(query)

# insert query
# insert_query = 'insert into emp(emp_id,name,salary,phone,email) ' \
#                'values(101,"amit",60000,"1234567891","amit@gamil.com")'
# conn.execute(insert_query)
# conn.commit()
'''
squery = 'select * from emp'
data = conn.execute(squery)

for d in data:
    print(d)
# ('amit', '1234567891', 'amit@gamil.com')
'''
# insert bulk data in the database
for i in range(101, 111, 1):
    fsalary = fk.random_int(6)
    fname = fk.first_name()
    fphone = fk.phone_number()
    femail = fk.email()
    dquery = f"insert into emp(emp_id,name,salary,phone,email) values('{i}','{fname}','{fsalary}','{fphone}','{femail}')"
    conn.execute(dquery)
    conn.commit()
conn.close()

# amit	1234567891	amit@gamil.com
# Molly	(673)207-3869x3407	garciacarrie@example.net
# Kirsten	347.393.4124x889	uhowell@example.org
# Teresa	337.883.4240	rayalexis@example.com
# Sarah	269.363.8014	ruizdonald@example.org
# Jon	001-507-497-1934x51533	joshualarsen@example.com
# Cassandra	(322)883-2607x4021	carlosjackson@example.net
# Shawn	(117)121-4470x0665	tonya41@example.org
# Andrew	9119681890	carlosgonzalez@example.org
# Rhonda	371.949.1561x51428	matthewvance@example.net
# Joseph	001-200-326-8280	kristinewhitehead@example.net
# Sheila	345-546-4997x351	serranojohn@example.org
# Cynthia	6585281566	kelly39@example.org
# Jennifer	001-701-276-1451x493	kelseyroberts@example.org
# Michael	454.091.5831x4783	iellis@example.net
# Christina	855.487.3871x3538	debra04@example.com
# Sharon	(011)593-9839	stephen98@example.net
# Laura	062.125.5057	rogerdavis@example.com
# Matthew	845.259.4769x655	snyderjames@example.com
# Connor	303.510.4221	savagejoshua@example.net
# Gloria	+1-542-689-2642x5221	stricklandbrian@example.com
# David	001-517-455-5794x0589	melissamercado@example.org
# Carmen	001-163-476-3387x52694	john97@example.com
# Juan	8572202468	xsantos@example.org
# Thomas	496.150.6455x654	wramirez@example.net
# David	527.526.1726x48882	toddperry@example.org
# Heather	524-504-2782	laurenallen@example.com
# Brandon	(857)326-8832x040	uadams@example.org
# Martin	485.525.3116x76303	smithgregory@example.net
# Judy	001-451-162-1617	jasminenelson@example.com
# James	001-402-148-6879	jessica71@example.net
# Traci	001-605-642-8269x8004	walkerrichard@example.com
# Anna	(148)322-0499	bgraham@example.org
# Mark	+1-453-134-8046x1429	paul45@example.org
# Christine	(211)134-8482x24672	shawndavenport@example.net
# Shawn	001-515-920-5065	cummingsjoseph@example.org
# Julie	(889)200-2899x5308	davidfisher@example.net
# Ashley	176.767.2960x6314	ashleygardner@example.net
# William	678.234.2606x5206	caleb61@example.org
# Ricardo	466-893-1060x43867	boonedavid@example.org
# Anna	3980357018	daniel79@example.com
# Karen	873.621.1340x73975	iramirez@example.org
# Bryan	717.710.9236x609	jamie76@example.com
# Nathan	001-101-705-6611x133	gonzalezhayley@example.org
# Robert	997-777-4501	michael68@example.com
# Eric	821-050-2813x3424	tadams@example.net
# Gary	+1-489-951-7519x153	taylormartin@example.com
# Lisa	8800664919	fchapman@example.com
# Michael	7550416751	marcuspowell@example.org
# Peter	+1-179-993-6712x796	austinmccoy@example.net
# Kristina	480.935.4279x59539	xrogers@example.com
# Joseph	462-286-9854x6262	amber65@example.com
# Marco	9001099893	garciaamanda@example.com
# William	400-503-7984	bgarcia@example.org
# James	407-547-6190x2355	bowmanrickey@example.net
# William	+1-236-648-3520x760	jonesmichelle@example.org
# Karen	666.715.7956x699	steven81@example.net
# Nicholas	(244)919-8117x41085	mmcmillan@example.org
# Elizabeth	(634)988-5981x85549	sjones@example.com
# John	(149)012-3520x4243	lukedaniels@example.org
# Kevin	114.188.2336x412	gmoran@example.org
# Katherine	348.726.0380	basschristopher@example.org
# Brad	013-834-1872x3643	alexandrahutchinson@example.net
# Amy	001-005-995-1685	toliver@example.net
# Crystal	605.451.6781	zmanning@example.net
# Jennifer	001-991-927-3024x81581	jessicapowell@example.com
# Laura	001-052-432-7682x391	chapmanjason@example.net
# Jason	511-298-6882x43604	thompsonjoseph@example.org
# Sheila	(825)714-9870x783	michaelmack@example.net
# Robert	001-975-487-9656x181	angelayoung@example.com
# Richard	561.519.5901x4664	priceamanda@example.net
# Lawrence	0602597497	darlenecrawford@example.net
# Jeremy	+1-215-469-5868x0141	theodorewhite@example.net
# Rachel	769-333-2546x756	allenrobert@example.net
# Teresa	001-677-694-8445x3673	rosewilliam@example.net
# Matthew	001-146-468-4726x330	mcguirerick@example.net
# Amy	001-174-009-7810x772	daviddelgado@example.org
# Denise	496-658-2615x7444	bethrichards@example.net
# Katie	001-890-053-5925x02810	justinochoa@example.com
# Julie	+1-984-843-0540x277	cynthiacurtis@example.com
# Ronald	485-214-9247x9567	gilesdustin@example.org
# Janice	397.489.4270x7115	allenmark@example.net
# Pamela	001-225-130-3291x81919	crodriguez@example.com
# Victoria	121-966-9378x1148	kwilliams@example.org
# Michael	001-803-309-1006x031	josephjohn@example.com
# Rebecca	679-374-6479x4156	kevinsandoval@example.net
# Belinda	001-581-393-1035x94433	michele92@example.net
# Melissa	(037)712-9669	jonesryan@example.org
# Dana	920.884.9007	jennifer85@example.net
# Dawn	+1-915-241-8934x4145	christina38@example.com
# Daniel	408-592-5467x92344	buchanankathleen@example.com
# Ryan	(999)375-5143x0420	nguyenevelyn@example.net
# Amanda	(586)657-3971	schroederamanda@example.net
# John	+1-185-043-0671	evan88@example.com
# Renee	1149482913	andersonjoseph@example.com
# Eric	(661)073-4275x97824	katelyn59@example.org
# Walter	428.133.6428x6189	kyle87@example.org
# Cheryl	547.196.8126x44652	bentleypatrick@example.net
# Douglas	(194)299-1602x080	kathryndouglas@example.org
# Kaylee	(417)106-6825x440	rhodeschristian@example.org
# John	(369)191-0704x38441	mmunoz@example.com