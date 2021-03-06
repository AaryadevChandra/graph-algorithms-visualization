# graph-algorithms-visualization
<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<!-- <br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Best-README-Template</h3>

  <p align="center">
    An awesome README template to jumpstart your projects!
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a>
  </p>
</div>
 -->


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

An algorithm visualizer is a program that uses graphics  based libraries and modules to simulate annd visualize the entire functioning of a particular algorithm; a graph algorithm visualizer is an algorithm visualizer specifically made for visualizing graph based algorithms.

<!-- Here's why:
* The project is made using pygame, networkx and numpy.
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should implement DRY principles to the rest of your life :smile:

Of course, no one template will serve all projects since your needs may be different. So I'll be adding more in the near future. You may also suggest changes by forking this repo and creating a pull request or opening an issue. Thanks to all the people have contributed to expanding this template!

Use the `BLANK_README.md` to get started. -->

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

This section contains a list of our major frameworks/libraries used to bootstrap our project.

* [Pygame](https://www.pygame.org/news)
* [NetworkX](https://networkx.org)
* [Numpy](https://numpy.org)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

To run the project go into the local cloned repository on your machine, and go into any one of the folders depending on which visualization you wish to run. 
Open a text editor/IDE of your choice and enter the same folder belonging to the respective visualization program. 

### Prerequisites

This project uses Pygame and NetworkX for the graphical components of the project and uses numpy for array and adjacency matrix related operations.
* Python 3+
* Pygame
* NetworkX
* Numpy

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/AaryadevChandra/graph-algorithms-visualization.git
   ```
2. Enter the folder belonging to the visualization you wish to run; and open a command line terminal inside that folder. 
3. Create a virtual environment before installing the required dependencies (Optional)
   **For Windows**
   ```sh
   py -3 -m venv .venv
   .venv\scripts\activate
   ```
   **For MacOS/Linux**
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
   
4. Use Pip to install the required dependencies
   ```sh
   pip install numpy
   pip install pygame
   pip install networkx
   ```

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

### Breadth First Search

For BFS, please open the BFS folder in a text editor/IDE of your choice and ensure that you have the required dependencies. Once this is done, run the `graphics.py` python file. 
After waiting for a couple seconds, you will be greeted by a pygame window displaying the visualization.

The visualization starts from `Node 0` and shall continue till all the nodes are discovered. 

No user input is required.

![caption](https://media.giphy.com/media/sizpUYi3fSU2njxVnA/giphy.gif)


### Dijkstra's 

The Dijkstra's algorithm implements single source shortest path algorithm to find the route from any node to any other node. Due to this nature, the user is required to input two valid inputs which are the `start_node` and `end_node` respectively. 

![caption](https://media.giphy.com/media/fdQhXtsNqaZsVCiVu5/giphy.gif)

Once this is done, the visualization then proceeds to show the actual relaxation of nodes at every iteration along with the visualization for checking the neighbours and adding new paths to the final routes. The visualization also marks discovered nodes as they are discovered. 


### Topological Sort
Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge u v, vertex u comes before v in the ordering. Topological Sorting for a graph is not possible if the graph is not a DAG.

In DFS, we print a vertex and then recursively call DFS for its adjacent vertices. In topological sorting, we need to print a vertex before its adjacent vertices. For example, in the given graph, the vertex ‘5’ should be printed before vertex ‘0’, but unlike DFS, the vertex ‘4’ should also be printed before vertex ‘0’. So Topological sorting is different from DFS. For example, a DFS of the shown graph is “5 2 3 1 0 4”, but it is not a topological sorting.

![capption](https://media.giphy.com/media/7o51GW5t6V7NoQe3ge/giphy.gif)

In the visualization above we are traversing through the graph to get the topological order of the graph.
The color codes are as follows: -
Green= Unvisited
Grey= Currently visiting/traversing
Blue=Visited

Starting from node 0, we check to see if has any outdegree which it doesn’t, and hence its directly pushed to stack. Same is the case for node 1. But in case of node 2, it has an edge directed towards node 3 which is unvisited and so we will visit node 3 which has an edge directed towards node 1 which is already visited. Now, node 3 is added to the stack followed by node 2. This repeats for all the nodes. Once all the nodes are visited, we print the stack in reverse. This is the topological order for the graph.
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

If you have a suggestion or a feature that you wish us to implement, or simply want to ask something or point something out; we'll be happy to hear from you!
Contact us on the below given socials.

[Aaryadev Chandra](https://www.linkedin.com/in/aaryadevchandra/) - aaryadevc@example.com

Project Link: [https://github.com/AaryadevChandra/graph-algorithms-visualization](https://github.com/AaryadevChandra/graph-algorithms-visualization)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

Use this space to list resources you find helpful and would like to give credit to. I've included a few of my favorites to kick things off!

* [Choose an Open Source License](https://choosealicense.com)
* [GitHub Emoji Cheat Sheet](https://www.webpagefx.com/tools/emoji-cheat-sheet)
* [Malven's Flexbox Cheatsheet](https://flexbox.malven.co/)
* [Malven's Grid Cheatsheet](https://grid.malven.co/)
* [Img Shields](https://shields.io)
* [GitHub Pages](https://pages.github.com)
* [Font Awesome](https://fontawesome.com)
* [React Icons](https://react-icons.github.io/react-icons/search)

<p align="right">(<a href="#top">back to top</a>)</p> -->



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
<!-- [contributors-shield]: https://img.shields.io/github/contributors/othneildrew/Best-README-Template.svg?style=for-the-badge
[contributors-url]: https://github.com/othneildrew/Best-README-Template/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/othneildrew/Best-README-Template.svg?style=for-the-badge
[forks-url]: https://github.com/othneildrew/Best-README-Template/network/members
[stars-shield]: https://img.shields.io/github/stars/othneildrew/Best-README-Template.svg?style=for-the-badge
[stars-url]: https://github.com/othneildrew/Best-README-Template/stargazers
[issues-shield]: https://img.shields.io/github/issues/othneildrew/Best-README-Template.svg?style=for-the-badge
[issues-url]: https://github.com/othneildrew/Best-README-Template/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/othneildrew/Best-README-Template/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/othneildrew
[product-screenshot]: images/screenshot.png
 -->
