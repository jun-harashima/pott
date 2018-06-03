====================================
How to find papers from the Internet
====================================

To find papers from the Internet, use ``search`` subcommand as follows:

.. code-block:: console

    $ pott search <KEYWORD>

Suppose that you are interested in BLEU, an evaluation metric for machine translation. You can find papers related to the word with:

.. code-block:: console

    $ pott search BLEU
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    | ID | PDF | FIRST AUTHOR | YEAR |                                      TITLE                                      |
    +====+=====+==============+======+=================================================================================+
    |  0 |   A | S An         | 1998 | Characterization of a novel subtype of human G protein-coupled receptor for     |
    |    |     |              |      | lysophosphatidic acid                                                           |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  1 |   A | K Papineni   | 2002 | BLEU: a method for automatic evaluation of machine translation                  |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  2 |   A | S An         | 1997 | Identification of cDNAs encoding two G protein‐coupled receptors for            |
    |    |     |              |      | lysosphingolipids                                                               |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  3 | N/A | S An         | 1997 | Molecular cloning of the human Edg2 protein and its identification as a         |
    |    |     |              |      | functional cellular receptor for lysophosphatidic acid                          |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  4 |   A | S An         | 2000 | Sphingosine 1-phosphate-induced cell proliferation, survival, and related       |
    |    |     |              |      | signaling events mediated by G protein-coupled receptors Edg3 and Edg5          |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  5 |   A | S An         | 1998 | Recombinant human G protein-coupled lysophosphatidic acid receptors mediate     |
    |    |     |              |      | intracellular calcium mobilization                                              |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  6 |   A | S An         | 1999 | Transduction of intracellular calcium signals through G protein-mediated        |
    |    |     |              |      | activation of phospholipase C by recombinant sphingosine 1-phosphate receptors  |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  7 |   A | C Callison-  | 2006 | Re-evaluation the role of bleu in machine translation research                  |
    |    |     | Burch        |      |                                                                                 |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  8 | N/A | …            | 1985 | Eczematous (irritant and allergic) reactions of the skin and barrier function   |
    |    |     |              |      | as determined by water vapour loss                                              |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  9 |   A | J Bleu       | 2012 | Evolution of female choosiness and mating frequency: effects of mating cost,    |
    |    |     |              |      | density and sex ratio                                                           |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    Input paper IDs, next or quit: 

pott uses `Google Scholar`_ to find papers for a given query. You can download a pdf for each paper with 'A' (available) in the PDF column. Input the ID to download a pdf:

.. _`Google Scholar`: https://scholar.google.com/

.. code-block:: console

    Input paper IDs, next or quit: 1
    Downloading "BLEU: a method for automatic evaluation of machine translation"
    Saved in the following location:
    /Users/john-smith/.pott/pdf/Papineni2002.pdf

The downloaded paper is named ``<AUTHOR NAME><YEAR>.pdf`` and saved in ``<HOME DIRECTORY>/.pott/pdf`` directory. When paper IDs with 'N/A' (not available) are given, pott asks again you to select other available paper IDs.

To see the next 10 search results, input 'next' (or 'n') instead of paper IDs. To quit the paper search, input 'quit' (or 'q') or use Ctrl+C.

Of course, you can use a phrase query with:

.. code-block:: console

    $ pott search machine translation
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    | ID | PDF | FIRST AUTHOR | YEAR |                                      TITLE                                      |
    +====+=====+==============+======+=================================================================================+
    |  0 |   A | P Koehn      | 2007 | Moses: Open source toolkit for statistical machine translation                  |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  1 |   A | K Papineni   | 2002 | BLEU: a method for automatic evaluation of machine translation                  |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  2 | N/A | H Somers     | 1999 | Example-based machine translation                                               |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  3 |   A | FJ Och       | 2003 | Minimum error rate training in statistical machine translation                  |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  4 |   A | PF Brown     | 1993 | The mathematics of statistical machine translation: Parameter estimation        |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  5 |   A | D Bahdanau   | 2014 | Neural machine translation by jointly learning to align and translate           |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  6 |   A | PF Brown     | 1990 | A statistical approach to machine translation                                   |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  7 | N/A | ML Forcada   | 2011 | Apertium: a free/open-source platform for rule-based machine translation        |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  8 |   A | K Cho        | 2014 | Learning phrase representations using RNN encoder-decoder for statistical       |
    |    |     |              |      | machine translation                                                             |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  9 |   A | P Duygulu    | 2002 | Object recognition as machine translation: Learning a lexicon for a fixed image |
    |    |     |              |      | vocabulary                                                                      |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    Input paper IDs, next or quit: 

To download multiple papers, input comma-separated paper IDs. In the above example, you can download papers about neural machine translation as shown below:

.. code-block:: console

    Input paper IDs, next or quit: 5,8
    Downloading "Neural machine translation by jointly learning to align and translate"
    Saved in the following location:
    /Users/john-smith/.pott/pdf/Bahdanau2014.pdf
    Downloading "Learning phrase representations using RNN encoder-decoder for statistical machine translation"
    Saved in the following location:
    /Users/john-smith/.pott/pdf/Cho2014.pdf

You can find recent papers using ``--year-low`` (or ``-yl``) option as follows:

.. code-block:: console

    $ pott search <KEYWORD> --year-low <YEAR>

In the following example, pott provides machine translation-related papers published after 2016.

.. code-block:: console

    $ pott search machine translation --year-low 2016
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    | ID | PDF | FIRST AUTHOR | YEAR |                                      TITLE                                      |
    +====+=====+==============+======+=================================================================================+
    |  0 |   A | Y Wu         | 2016 | Google's neural machine translation system: Bridging the gap between human and  |
    |    |     |              |      | machine translation                                                             |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  1 |   A | F Stahlberg  | 2018 | Why not be Versatile? Applications of the SGNMT Decoder for Machine Translation |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  2 |   A | J Chung      | 2016 | A character-level decoder without explicit segmentation for neural machine      |
    |    |     |              |      | translation                                                                     |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  3 |   A | MT Luong     | 2016 | Achieving open vocabulary neural machine translation with hybrid word-character |
    |    |     |              |      | models                                                                          |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  4 | N/A | F Hill       | 2017 | The representational geometry of word meanings acquired by neural machine       |
    |    |     |              |      | translation models                                                              |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  5 |   A | R Sennrich   | 2017 | Nematus: a toolkit for neural machine translation                               |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  6 |   A | R Sennrich   | 2016 | Edinburgh neural machine translation systems for wmt 16                         |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  7 | N/A |              |      |                                                                                 |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  8 |   A | O Firat      | 2016 | Multi-way, multilingual neural machine translation with a shared attention      |
    |    |     |              |      | mechanism                                                                       |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    |  9 |   A | M Johnson    | 2016 | Google's multilingual neural machine translation system: enabling zero-shot     |
    |    |     |              |      | translation                                                                     |
    +----+-----+--------------+------+---------------------------------------------------------------------------------+
    Input paper IDs, next or quit: 

On the other hand, ``--year-high`` (or ``/-yh``) option finds papers published before a specified year.

.. code-block:: console

    $ pott search <KEYWORD> --year-high <YEAR>
