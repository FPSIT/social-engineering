## Scenario

Albertine is a disgruntled student who was rejected from an internship position at the RudolphRedNose Fictional Research Group.

Albertine talked to Matt Giallourakis, the Chief Technology Officer of RudolphRedNose at the Dorifla Tolypechnic career fair. In their discussion, Albertine learned about the tech stack used by R.R.N. To analyze climate data, R.R.N. uses the R language, Tableau, and Python3. One of Matts’ favorite technologies, Jupyter Notebooks, was used to demo some of the newest findings published by R.R.N. Albertine took special note of this at the career fair, and began to plan an attack after being rejected.

Matt Giallourakis is an alumni of Dorifla Tolypechnic. He graduated as a data scientist with a concentration in environmental science. As an avid python user interested in graphical models, he makes good use of Tableau and Jupyter notebooks, especially for internal demonstrations. Matt runs Windows 10 on his company-issued laptop, which Albertine also noticed. R.R.N. has restrictive security policies and does not allow users to install software from outside sources. All software must be approved and made available through the R.R.N. package manager. Once a software or tool is approved for use, it is made available to users through the package manager.

Albertine knows that to carry out a successful attack, the R.R.N. network must be entered through either social engineering or through a backdoor. Albertine decides to enter the network via social engineering, by eventually fooling Matt. Matt isn't foolish, but Albertine might be creative enough to carry out a successful attack with a few key tricks.

#### Scenario 1 – A successful attack

The Python3 basic install includes pip3, the python package manager. It also includes a module called `system`, which Albertine will use to arbitrarily execute shell commands on a victims machine, at the access level the victim is cleared for. Albertine doesn't know what Matts access level is, and won't take a gamble. Albertine knows that Matt must surely have permissions to run python, and also remembers that programs can have single-user installation. Based on this knowledge, he creates a malicious script, and finds a way to run it on Matts machine.

At R.R.N. each team member completes information assurance training. Team members can differentiate between spam emails and phishing attempts. External emails are marked as `[external]` in the subject line by the windows mail server.

information on phishing attempts and red flags https://staysafeonline.org/blog/5-ways-spot-phishing-emails/
information on spam https://www.liquidweb.com/blog/5-tips-to-identify-dangerous-spam-emails/

Matt receives this message:

```
[external] Bringing the best out of Jupyter Notebooks for Data Science
from: datascientists@jupyter.design
to:   dsimailinglist@jupyter.design
bcc:  mgiallourakis@rrn.llc

Hi all,

I wanted to share a short read that one of our contributors put together. The Jupyter project has always aimed to make data beautiful, and we have always believed that Jupyter Notebooks is the ideal open source software to fill that need. Thank you for using Jupyter Notebooks; we hope to see continued creative solutions from our open source community.

If you have any suggestions regarding the direction of the Jupyter Notebook project, submit a pull request while following the contribution guidelines here: https://github.com/jupyter/help

You are also welcome to message the steering council with more significant concerns (please use business email addresses) https://jupyter.org/about

(Article) Parul Pandey, Towards Data Science
https://towardsdatascience.com/bringing-the-best-out-of-jupyter-notebooks-for-data-science-f0871519ca29

Kind regards,


Caleb Shepard
github.com/Caleb-Shepard
```

When Matt reads this message, he recognizes it as a potential spam newsletter. There is no external link leading to a download or login, no call to action, and the article looks well written. Matt has read articles from towardsdatascience.com before and the content seems informative and helpful. When Matt looks up the sender on GitHub, he sees that the sender is indeed a contributor to the Jupyter Notebooks codebase. The message isn't dangerous and isn't a phishing attempt, so he doesn't unsubscribe from the mailing list. This seems like a mailing list that probably isn't used frequently anyway.

One week later, Matt receives another email from this sender.

```
[external] Jupyter Notebooks x Climate Science
from:  cshepard@jupyter.design
to:    mgiallourakis@rrn.llc

Hi Matt,

The Jupyter Notebooks team has been looking at the best public projects that make use of Jupyter Notebooks. Your demonstrated work on cloud simulation is outstanding and we would like to extend the Notebook project to include modules that display geographically dependent data. A small team of Jupyter contributors have forked gmaps to fulfill this role. It is important for us to respond to feedback that you and other experts in climate science provide us with. The open source community that made the Jupyter project shares the love for knowledge that its users have, and we want to kindly invite you to collaborate on this venture as a functional tester.

gmaps master branch https://github.com/pbugnion/gmaps
jupyter-cmaps       https://github.com/foldsters/jupyter-cmaps

Kind regards,


Caleb Shepard
github.com/Caleb-Shepard
```

#### Scenario 2 – Ignorance

Matt reads or skims the emails and deletes them.

#### Scenario 3 – Aversion

When Matt finds an external dependency, he examines it himself. Even if the dependency is on GitHub, he knows that it might introduce malicious python.
