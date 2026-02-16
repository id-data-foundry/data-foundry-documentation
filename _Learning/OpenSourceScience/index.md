---
layout: default
title: Open Source and Science
nav_order: 4
has_children: true
has_toc: true
---

# Open Source and Science

Open Science is a movement within academia to democratize scientific research and make knowledge publicly accessible. Access to knowledge is often restricted to those who can afford expensive subscriptions to major publishers, even when research is publicly funded. Open Science aims to change this by promoting the open sharing of knowledge. This not only makes research more accessible but also promotes a more transparent research process, making it easier for third parties to validate data and fostering collaboration between researchers.

Open Science is more than just freely sharing data and knowledge; it also involves building freely accessible tools to collect, process, and analyze data. This allows anyone to validate results or reinterpret data without needing expensive software or starting from scratch.

## Open Source

Open Source software is similar, aiming to make software freely accessible (Free as in freedom), allowing anyone to modify, contribute and inspect code. Open Sourcing your software helps with transparency as anyone can inspect what the software is actually doing, and allows anyone to build forward on your software. Open Source projects are usually community driven and often rely on volunteers to keep operating. 

Some companies also open-source their software, often with the intention that the community will maintain the software. This is done by removing bugs and keeping things compatible. Not all Open Source software is the same however as this mostly depends on the license a software is published under. [You can find more information about the licenses used on Data Foundry here.]({% link _Learning/OpenSourceScience/LicenseIntro.md %})


Open Source software shall be:
- Free to Redistribute (free as in everyone should be allowed to redistribute not per say without payment).
- Have accessible source code, which can also be freely distributed.
- Allow for sharing of modified and derived works (under the same license as the original) OR allow for patches that can modify the original work.
- Freely accessible to anyone in any context with any technology.
- Work without needing relying on non freely licensed software and cant impose additional restrictions.
- The License of the software can not restrict other software that is distributed along.

For more information on the official definitions, visit the [Open Source Initiative website](https://opensource.org/osd).

### Challenges and Security

While open source offers many benefits, it also presents challenges. Many large projects depend on small packages maintained by individuals, which can create single points of failure. 

Because everyone can contribute, there is a theoretical risk of malicious contributions. This is why it is crucial for sensitive open source code to be well-moderated, transparent, and peer-reviewed. Popular projects benefit from having many eyes on the code, which helps identify and mitigate security vulnerabilities.

### Version Control with Git

Open source source code is typically hosted on platforms like GitHub, GitLab, or Codeberg. These platforms provide tools to organize changes and foster collaboration using the Git version control protocol.
Git makes collaborating on code easier by keeping track of changes and structuring how code is added or removed. Back in the day git was used over email. But nowadays most people use the aforementioned platforms. It is important to take in mind that not all code of github and gitlab is actually Open Source.

## Open Weights

Because the AI model market is still super competitive and mainly driven by for-profit companies, these companies are not always sharing their proprietary source code with the rest of the world. Openly sharing the source code of your AI model would allow other companies to copy your work and walk with it. That's why these companies often work with Open Weight models. Open Weight AI models are essentially the final product of the AI training process, and can be freely shared without accidentally revealing the proprietary training process itself. This makes it that these models can be used and tweaked by anyone, however without the ability to replicating or create derived works.
