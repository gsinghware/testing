<h1>Homework 1: CSc 599.69 Visualization, Fall 2014</h1><h2 id="homework-csc-599-69-visualization-fall-2014-due-thurs-sept-11th">Homework : CSc 599.69 Visualization, Fall 2014, Due Thurs Sept. 11th</h2><table><tr><td class="field-label">Instructor</td><td><p>Michael Grossberg</p></td></tr></table><p>Note: Do <strong>not</strong> submit Microsoft Word,
Open Office, Pages or PDF. Submit
plain text documents only or
don't bother submitting.</p><section id="problem-1-introduce-yourself"><header><h2>Problem 1: Introduce yourself</h2></header><p>Answer several questions about yourself in the blackboard:</p><ol class="loweralpha"><li><p>What languages did you program in?</p></li><li><p>Do you have experience with scientific python/matplotlib?</p></li><li><p>What visualizations have you made?</p></li><li><p>What tools did you use to make them?</p></li><li><p>What data do you dream of visualizing?</p></li></ol><p>This will be in a discussion thread of blackboard.</p></section><section id="problem-2-dvcs"><header><h2>Problem 2: DVCS</h2></header><p>There will be a place to submit the link
to your repo on blackboard.</p><p>In this problem you will set up a Bitbucket
account. Create a local repository. Modify
some files, make some commits and push
to bitbucket. Since this is fundamental
to the course, if you cannot figure out,
or find the time to do this, you should
drop the course immediately.</p><section id="background"><header><h3>Background</h3></header><p>Modern professional programmers live and die
by distributed version control systems. Version
control provides backup, and the freedom to
make changes and undo them. More than that,
it makes it easy for large groups of people
to remotely collaborate.</p><p>Remote collaboration is very important
in professional settings where programmers
and designers, working on a project,
may be spread across the globe. It is
even more crucial in open source project
where remote collaborations are even
more common.</p><p>There are a few full featured, performant
Distributed version control systems (DCVS). The
two most popular are Git, and Mercurial.
Git was Linus Torvalds, the developer
of Linux. It is probably the most popular
one, and has many technical advantages. It
is also notoriously complex, and difficult
for beginners. Mercurial has most of the
core functionality of Git but is much simpler
to use. For this reason we will use
Mercurial.</p></section><section id="problem"><header><h3>Problem</h3></header><ol class="arabic"><li><p>Create an account on bitbucket. You can
set up a free account at</p><blockquote><p><a class="reference external" href="https://bitbucket.org/">https://bitbucket.org/</a></p></blockquote><p>The bitbucket site has documentation
which you should read. In addition
the syllabus gives links to Mercurial (aka hg)
tutorials and documentation.</p></li><li><p>Create a new repository called csc59969F14hw1. (private)</p></li><li><p>Clone you repository to your local directory.
On mac or linux you can just use the hg command line
command. This is possible on windows as well but
slightly tricker to install. You may want to use
tortoisehg on windows or possibly even on Mac</p><p><a class="reference external" href="http://tortoisehg.bitbucket.org/">http://tortoisehg.bitbucket.org/</a></p></li><li><p>Use a <strong>text</strong> editor. Free ones include
as notepad++ (windows), textwrangler (mac),
kate/gedit (linux), emacs or vim (all platforms)
to create a file called ".hgignore" which should
look like this:</p><pre># use glob syntax.
      syntax: glob

      **.pyc
      **~</pre></li><li><p>Use a <strong>text</strong> editor such as notepad++ (windows),
textwrangler (mac), kate (linux),
emacs or vim (all platforms) to create a file called
"hw1_problem_1.txt" with Lincoln's Gettysburg Address:</p><pre>            Four score and seven years ago our fathers brought
forth on this continent, a new nation, conceived in
Liberty, and dedicated to the proposition that all men
are created equal.

            Now we are engaged in a great civil war, testing
whether that nation,    or any nation so conceived
and so dedicated, can long endure. We are met on a
great battle-field of that war. We have come to
dedicate a portion of that field, as a final resting
place for those who here gave their lives that that
nation might live. It is altogether fitting and proper
that we should do this.

            But, in a larger sense, we can not dedicate -- we can
not consecrate --       we can not hallow -- this ground.
The brave men, living and dead, who     struggled here,
have consecrated it, far above our poor power to add
or detract. The world will little note, nor long
remember what we say here, but it can never forget
what they did here. It is for us the    living, rather,
to be dedicated here to the unfinished work which they
who fought here have thus far so nobly advanced. It is
rather for us to be here dedicated to the great task
remaining before us -- that from these honored dead we
take increased devotion to that cause for       which they
gave the last full measure of devotion -- that we here
highly resolve that these dead shall not have died in
vain -- that this nation, under God, shall have a new
birth of freedom -- and that government of the people,
by the people, for the people, shall not perish from
the earth.</pre></li><li><p>Add it to repo with the command "hg add", then commit it
to the repo using</p><blockquote><blockquote><p>hg commit -m "This is my initial commit"</p></blockquote><p>If you forget to use the "-m" with a message you will find
yourself in editor, most likely vi. Then you have to write
your commit message.</p></blockquote></li><li><p>Push it to bitbucket with the command "hg push"</p></li><li><p>Modify the file by replacing the Gettysburg Address with
the poem, 'The New Colossus' (see wikipedia):</p><pre>Not like the brazen giant of Greek fame,
With conquering limbs astride from land to land;
Here at our sea-washed, sunset gates shall stand
A mighty woman with a torch, whose flame
Is the imprisoned lightning, and her name
Mother of Exiles. From her beacon-hand
Glows world-wide welcome; her mild eyes command
The air-bridged harbor that twin cities frame.
"Keep, ancient lands, your storied pomp!" cries she
With silent lips. "Give me your tired, your poor,
Your huddled masses yearning to breathe free,
The wretched refuse of your teeming shore.
Send these, the homeless, tempest-tost to me,
I lift my lamp beside the golden door!</pre></li><li><p>Commit the changes to the repository.</p></li><li><p>Push the change to bitbucket.</p></li><li><p>Invite me and the grading robot
to share your bitbucket hw repository,
my bitbucket username is "mdogy"
and the grading robot's bitbucket
username is "teamglass7311". Do not use
my ccny email or my gmail account. Use these
two usernames on bitbucket.</p></li><li><p>On blackboard, when asked to enter the bitbucket url, enter
the information in a single line with nothing else.
It should look like this:</p><pre>ssh://hg@bitbucket.org/yourbitbucketusername/csc59969F14hw1</pre><p>where you change yourbitbucketusername to your bitbucket username
and you put your homework for homework1 in a repo called:</p><p>csc59969F14hw1</p></li></ol></section></section><section id="problem-3-design-critique"><header><h2>Problem 3: Design Critique</h2></header><p>Create a thread on blackboard to answer this question.
Here is a source of good visualizations:</p><p><a class="reference external" href="http://flowingdata.com/">http://flowingdata.com/</a></p><p>and a source of less good ones:</p><p><a class="reference external" href="http://wtfviz.net/">http://wtfviz.net/</a></p><p>Please pick and critique one good (from flowing data)
and one less good (from wtfviz) visualization.</p><p>Label and answer each of the following questions.
Looking for at least 2 sentences per question. Be specific.
Vague answers that lack depth will lose points.</p><ol class="arabic"><li><p>Who is the audience? (expert? non-expert?)</p></li><li><p>What questions does this visualization answer?</p></li><li><p>What design principles best describe why it is good / bad?</p></li><li><p>Why do you like / dislike this visualization?</p></li><li><p>Can you suggest any improvements?</p></li></ol><p>Make a separate thread for each visualization (total 2 threads)
and link to the visualization. Comment on two other students critiques
(agree/disagree). In your comment you must make a significant points.
Don't just say "cool", or "dude that sucks".</p></section><section id="problem-4-make-a-line-plot-in-python"><header><h2>Problem 4: Make a line plot in Python</h2></header><p>We will make some simple line plots in matplotlib. We will use
data from the Food and Agriculture Organization (FAO) made
available at the United Nation data site.</p><p><a class="reference external" href="http://data.un.org/Explorer.aspx?d=FAO&amp;f=itemCode%3a1079">http://data.un.org/Explorer.aspx?d=FAO&amp;f=itemCode%3a1079</a></p><p>Use the FAO data under live stock to extract time series for
the population of the goats in the continents Africa, North America,
South America, Asia, Europe and Austrailia + New Zeland.
The time series data is yearly and goes from the early 1960's to
around 2007.</p><p>Download the data as in csv form. Use the python csv library and
in particular csv.DictReader to read the data.</p><p>Once you have a time series for each continent make a single
line plot where each continent has a different color. Make
sure you label every axis with a tick for each year. Make sure
that you give the graph an informative title and put text on the
graph identifying the source of the data. In the line plot don't
put markers at the data points, just solid lines.</p></section><section id="problem-5-make-a-bar-graph-in-python"><header><h2>Problem 5: Make a bar graph in Python</h2></header><p>Go back to the FAO data from problem 4. Just look at data from
2007. Make a separate bar graph for each of the continents comparing
the number of pigs, ducks, goats, sheep, cattle, chickents and turkeys.
That will be 6 bar graphs with 7 bars each. Now, try to find a way to
combine these in a single graph. How will you show continent vs. animal?</p></section>
