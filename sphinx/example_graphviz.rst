Sample graphviz chapter
=======================

General information
-------------------
The documentation to graphviz and thus an explanation how to generate this graphs is available under: https://www.graphviz.org/pdf/dotguide.pdf

Further, an free online editor can be accessed via: https://dreampuf.github.io/GraphvizOnline

An idea could be to write a short python script which can be called in order to automatically generate this graphs.
Otherwise, they need to be generated in the "sphinx" folder just via the shell command "make html".

.. attention::
    Besides "**pip install graphviz**" to the desired environment, which may causes some issues, it is recommend to install
    it via "**sudo apt-get install graphviz**".

Diagram 1
---------
At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti
quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia
deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.

.. graphviz::

    digraph G {
        size ="4,4";
        main [shape=box]; /* this is a comment */
        main -> parse [weight=8];
        parse -> execute;
        main -> init [style=dotted];
        main -> cleanup;
        execute -> { make_string; printf}
        init -> make_string;
        edge [color=red]; // so is this
        main -> printf [style=bold,label="100 times"];
        make_string [label="make a\nstring"];
        node [shape=box,style=filled,color=".7 .3 1.0"];
        execute -> compare;
    }


Diagram 2
---------
At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti
quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia
deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.

.. graphviz::

    digraph H {
        "Step A" -> "Step B" -> "Step C";
        "Step B" -> "Step A";
    }


Diagram 3
---------
At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium voluptatum deleniti atque corrupti
quos dolores et quas molestias excepturi sint occaecati cupiditate non provident, similique sunt in culpa qui officia
deserunt mollitia animi, id est laborum et dolorum fuga. Et harum quidem rerum facilis est et expedita distinctio.

.. graphviz::

    digraph J {

        subgraph cluster_0 {
            style=filled;
            color=lightgrey;
            node [style=filled,color=white];
            a0 -> a1 -> a2 -> a3;
            label = "process #1";
        }

        subgraph cluster_1 {
            node [style=filled];
            b0 -> b1 -> b2 -> b3;
            label = "process #2";
            color=blue
        }
        start -> a0;
        start -> b0;
        a1 -> b3;
        b2 -> a3;
        a3 -> a0;
        a3 -> end;
        b3 -> end;

        start [shape=Mdiamond];
        end [shape=Msquare];
    }