"""Data RAG Example - Complete setup in one file"""

import os
from core.document import Document
from core.rag_service import RAGService
from core.embedders.sentence_transformer_embedder import SentenceTransformerEmbedder
from core.vector_stores.chroma_vector_store import ChromaVectorStore

# Example documents
DOCUMENTS = [
Document(
    title="The Matrix (1999)",
    content="""Type: Movie
        Title: The Matrix
        Released: 1999
        Tagline: "Welcome to the Real World"

        Cast:
        - Keanu Reeves as Neo
        - Carrie-Anne Moss as Trinity
        - Laurence Fishburne as Morpheus
        - Hugo Weaving as Agent Smith
        - Emil Eifrem as Emil

        Directors:
        - Lilly Wachowski
        - Lana Wachowski

        Producers:
        - Joel Silver
        """
    ),

Document(
    title="The Matrix Reloaded (2003)",
    content="""Type: Movie
        Title: The Matrix Reloaded
        Released: 2003
        Tagline: "Free your mind"

        Cast:
        - Keanu Reeves as Neo
        - Carrie-Anne Moss as Trinity
        - Laurence Fishburne as Morpheus
        - Hugo Weaving as Agent Smith

        Directors:
        - Lilly Wachowski
        - Lana Wachowski

        Producers:
        - Joel Silver
        """
    ),

Document(
    title="The Matrix Revolutions (2003)",
    content="""Type: Movie
        Title: The Matrix Revolutions
        Released: 2003
        Tagline: "Everything that has a beginning has an end"

        Cast:
        - Keanu Reeves as Neo
        - Carrie-Anne Moss as Trinity
        - Laurence Fishburne as Morpheus
        - Hugo Weaving as Agent Smith

        Directors:
        - Lilly Wachowski
        - Lana Wachowski

        Producers:
        - Joel Silver
        """
    ),

Document(
    title="The Devil's Advocate (1997)",
    content="""Type: Movie
        Title: The Devil's Advocate
        Released: 1997
        Tagline: "Evil has its winning ways"

        Cast:
        - Keanu Reeves as Kevin Lomax
        - Charlize Theron as Mary Ann Lomax
        - Al Pacino as John Milton

        Directors:
        - Taylor Hackford
        """
    ),

Document(
    title="A Few Good Men (1992)",
    content="""Type: Movie
        Title: A Few Good Men
        Released: 1992
        Tagline: "In the heart of the nation's capital, in a courthouse of the U.S. government, one man will stop at nothing to keep his honor, and one will stop at nothing to find the truth."

        Cast:
        - Tom Cruise as Lt. Daniel Kaffee
        - Jack Nicholson as Col. Nathan R. Jessup
        - Demi Moore as Lt. Cdr. JoAnne Galloway
        - Kevin Bacon as Capt. Jack Ross
        - Kiefer Sutherland as Lt. Jonathan Kendrick
        - Noah Wyle as Cpl. Jeffrey Barnes
        - Cuba Gooding Jr. as Cpl. Carl Hammaker
        - Kevin Pollak as Lt. Sam Weinberg
        - J.T. Walsh as Lt. Col. Matthew Andrew Markinson
        - James Marshall as Pfc. Louden Downey
        - Christopher Guest as Dr. Stone
        - Aaron Sorkin as Man in Bar

        Directors:
        - Rob Reiner

        Writers:
        - Aaron Sorkin
        """
    ),

Document(
    title="Top Gun (1986)",
    content="""Type: Movie
        Title: Top Gun
        Released: 1986
        Tagline: "I feel the need, the need for speed."

        Cast:
        - Tom Cruise as Maverick
        - Kelly McGillis as Charlie
        - Val Kilmer as Iceman
        - Anthony Edwards as Goose
        - Tom Skerritt as Viper
        - Meg Ryan as Carole

        Directors:
        - Tony Scott

        Writers:
        - Jim Cash
        """
    ),

Document(
    title="Jerry Maguire (2000)",
    content="""Type: Movie
        Title: Jerry Maguire
        Released: 2000
        Tagline: "The rest of his life begins now."

        Cast:
        - Tom Cruise as Jerry Maguire
        - Cuba Gooding Jr. as Rod Tidwell
        - Renee Zellweger as Dorothy Boyd
        - Kelly Preston as Avery Bishop
        - Jerry O'Connell as Frank Cushman
        - Jay Mohr as Bob Sugar
        - Bonnie Hunt as Laurel Boyd
        - Regina King as Marcee Tidwell
        - Jonathan Lipnicki as Ray Boyd

        Directors:
        - Cameron Crowe

        Producers:
        - Cameron Crowe

        Writers:
        - Cameron Crowe

        Reviews:
        - Jessica Thompson rated it 92/100: "You had me at Jerry"
        """
    ),

Document(
    title="Stand By Me (1986)",
    content="""Type: Movie
        Title: Stand By Me
        Released: 1986
        Tagline: "For some, it's the last real taste of innocence, and the first real taste of life. But for everyone, it's the time that memories are made of."

        Cast:
        - Wil Wheaton as Gordie Lachance
        - River Phoenix as Chris Chambers
        - Jerry O'Connell as Vern Tessio
        - Corey Feldman as Teddy Duchamp
        - John Cusack as Denny Lachance
        - Kiefer Sutherland as Ace Merrill
        - Marshall Bell as Mr. Lachance

        Directors:
        - Rob Reiner
        """
    ),

Document(
    title="As Good as It Gets (1997)",
    content="""Type: Movie
        Title: As Good as It Gets
        Released: 1997
        Tagline: "A comedy from the heart that goes for the throat."

        Cast:
        - Jack Nicholson as Melvin Udall
        - Helen Hunt as Carol Connelly
        - Greg Kinnear as Simon Bishop
        - Cuba Gooding Jr. as Frank Sachs

        Directors:
        - James L. Brooks
        """
    ),

Document(
    title="What Dreams May Come (1998)",
    content="""Type: Movie
        Title: What Dreams May Come
        Released: 1998
        Tagline: "After life there is more. The end is just the beginning."

        Cast:
        - Robin Williams as Chris Nielsen
        - Cuba Gooding Jr. as Albert Lewis
        - Annabella Sciorra as Annie Collins-Nielsen
        - Max von Sydow as The Tracker
        - Werner Herzog as The Face

        Directors:
        - Vincent Ward
        """
    ),

Document(
    title="Snow Falling on Cedars (1999)",
    content="""Type: Movie
        Title: Snow Falling on Cedars
        Released: 1999
        Tagline: "First loves last. Forever."

        Cast:
        - Ethan Hawke as Ishmael Chambers
        - Rick Yune as Kazuo Miyamoto
        - Max von Sydow as Nels Gudmundsson
        - James Cromwell as Judge Fielding

        Directors:
        - Scott Hicks
        """
    ),

Document(
    title="You've Got Mail (1998)",
    content="""Type: Movie
        Title: You've Got Mail
        Released: 1998
        Tagline: "At odds in life... in love on-line."

        Cast:
        - Tom Hanks as Joe Fox
        - Meg Ryan as Kathleen Kelly
        - Greg Kinnear as Frank Navasky
        - Parker Posey as Patricia Eden
        - Dave Chappelle as Kevin Jackson
        - Steve Zahn as George Pappas

        Directors:
        - Nora Ephron
        """
    ),

Document(
    title="Sleepless in Seattle (1993)",
    content="""Type: Movie
        Title: Sleepless in Seattle
        Released: 1993
        Tagline: "What if someone you never met, someone you never saw, someone you never knew was the only someone for you?"

        Cast:
        - Tom Hanks as Sam Baldwin
        - Meg Ryan as Annie Reed
        - Rita Wilson as Suzy
        - Bill Pullman as Walter
        - Victor Garber as Greg
        - Rosie O'Donnell as Becky

        Directors:
        - Nora Ephron
        """
    ),

Document(
    title="Joe Versus the Volcano (1990)",
    content="""Type: Movie
        Title: Joe Versus the Volcano
        Released: 1990
        Tagline: "A story of love, lava and burning desire."

        Cast:
        - Tom Hanks as Joe Banks
        - Meg Ryan as DeDe, Angelica Graynamore, Patricia Graynamore
        - Nathan Lane as Baw

        Directors:
        - John Patrick Stanley
        """
    ),

Document(
    title="When Harry Met Sally (1998)",
    content="""Type: Movie
        Title: When Harry Met Sally
        Released: 1998
        Tagline: "Can two friends sleep together and still love each other in the morning?"

        Cast:
        - Billy Crystal as Harry Burns
        - Meg Ryan as Sally Albright
        - Carrie Fisher as Marie
        - Bruno Kirby as Jess

        Directors:
        - Rob Reiner

        Producers:
        - Rob Reiner
        - Nora Ephron

        Writers:
        - Nora Ephron
        """
    ),

Document(
    title="That Thing You Do (1996)",
    content="""Type: Movie
        Title: That Thing You Do
        Released: 1996
        Tagline: "In every life there comes a time when that thing you dream becomes that thing you do"

        Cast:
        - Tom Hanks as Mr. White
        - Liv Tyler as Faye Dolan
        - Charlize Theron as Tina

        Directors:
        - Tom Hanks
        """
    ),

Document(
    title="The Replacements (2000)",
    content="""Type: Movie
        Title: The Replacements
        Released: 2000
        Tagline: "Pain heals, Chicks dig scars... Glory lasts forever"

        Cast:
        - Keanu Reeves as Shane Falco
        - Brooke Langton as Annabelle Farrell
        - Gene Hackman as Jimmy McGinty
        - Orlando Jones as Clifford Franklin

        Directors:
        - Howard Deutch

        Reviews:
        - Jessica Thompson rated it 65/100: "Silly, but fun"
        - James Thompson rated it 100/100: "The coolest football movie ever"
        - Angela Scope rated it 62/100: "Pretty funny at times"
        """
    ),

Document(
    title="RescueDawn (2006)",
    content="""Type: Movie
        Title: RescueDawn
        Released: 2006
        Tagline: "Based on the extraordinary true story of one man's fight for freedom"

        Cast:
        - Marshall Bell as Admiral
        - Christian Bale as Dieter Dengler
        - Zach Grenier as Squad Leader
        - Steve Zahn as Duane

        Directors:
        - Werner Herzog
        """
    ),

Document(
    title="The Birdcage (1996)",
    content="""Type: Movie
        Title: The Birdcage
        Released: 1996
        Tagline: "Come as you are"

        Cast:
        - Robin Williams as Armand Goldman
        - Nathan Lane as Albert Goldman
        - Gene Hackman as Sen. Kevin Keeley

        Directors:
        - Mike Nichols

        Reviews:
        - Jessica Thompson rated it 45/100: "Slapstick redeemed only by the Robin Williams and Gene Hackman's stellar performances"
        """
    ),

Document(
    title="Unforgiven (1992)",
    content="""Type: Movie
        Title: Unforgiven
        Released: 1992
        Tagline: "It's a hell of a thing, killing a man"

        Cast:
        - Richard Harris as English Bob
        - Clint Eastwood as Bill Munny
        - Gene Hackman as Little Bill Daggett

        Directors:
        - Clint Eastwood

        Reviews:
        - Jessica Thompson rated it 85/100: "Dark, but compelling"
        """
    ),

Document(
    title="Johnny Mnemonic (1995)",
    content="""Type: Movie
        Title: Johnny Mnemonic
        Released: 1995
        Tagline: "The hottest data on earth. In the coolest head in town"

        Cast:
        - Keanu Reeves as Johnny Mnemonic
        - Takeshi Kitano as Takahashi
        - Dina Meyer as Jane
        - Ice-T as J-Bone

        Directors:
        - Robert Longo
        """
    ),

Document(
    title="Cloud Atlas (2012)",
    content="""Type: Movie
        Title: Cloud Atlas
        Released: 2012
        Tagline: "Everything is connected"

        Cast:
        - Tom Hanks as Zachry, Dr. Henry Goose, Isaac Sachs, Dermot Hoggins
        - Hugo Weaving as Bill Smoke, Haskell Moore, Tadeusz Kesselring, Nurse Noakes, Boardman Mephi, Old Georgie
        - Halle Berry as Luisa Rey, Jocasta Ayrs, Ovid, Meronym
        - Jim Broadbent as Vyvyan Ayrs, Captain Molyneux, Timothy Cavendish

        Directors:
        - Tom Tykwer
        - Lilly Wachowski
        - Lana Wachowski

        Producers:
        - Stefan Arndt

        Writers:
        - David Mitchell

        Reviews:
        - Jessica Thompson rated it 95/100: "An amazing journey"
        """
    ),

Document(
    title="The Da Vinci Code (2006)",
    content="""Type: Movie
        Title: The Da Vinci Code
        Released: 2006
        Tagline: "Break The Codes"

        Cast:
        - Tom Hanks as Dr. Robert Langdon
        - Ian McKellen as Sir Leight Teabing
        - Audrey Tautou as Sophie Neveu
        - Paul Bettany as Silas

        Directors:
        - Ron Howard

        Reviews:
        - Jessica Thompson rated it 68/100: "A solid romp"
        - James Thompson rated it 65/100: "Fun, but a little far fetched"
        """
    ),

Document(
    title="V for Vendetta (2006)",
    content="""Type: Movie
        Title: V for Vendetta
        Released: 2006
        Tagline: "Freedom! Forever!"

        Cast:
        - Hugo Weaving as V
        - Natalie Portman as Evey Hammond
        - Stephen Rea as Eric Finch
        - John Hurt as High Chancellor Adam Sutler
        - Ben Miles as Dascomb

        Directors:
        - James Marshall

        Producers:
        - Lilly Wachowski
        - Lana Wachowski
        - Joel Silver

        Writers:
        - Lilly Wachowski
        - Lana Wachowski
        """
    ),

Document(
    title="Speed Racer (2008)",
    content="""Type: Movie
        Title: Speed Racer
        Released: 2008
        Tagline: "Speed has no limits"

        Cast:
        - Emile Hirsch as Speed Racer
        - John Goodman as Pops
        - Susan Sarandon as Mom
        - Matthew Fox as Racer X
        - Christina Ricci as Trixie
        - Rain as Taejo Togokahn
        - Ben Miles as Cass Jones

        Directors:
        - Lilly Wachowski
        - Lana Wachowski

        Producers:
        - Joel Silver

        Writers:
        - Lilly Wachowski
        - Lana Wachowski
        """
    ),

Document(
    title="Ninja Assassin (2009)",
    content="""Type: Movie
        Title: Ninja Assassin
        Released: 2009
        Tagline: "Prepare to enter a secret world of assassins"

        Cast:
        - Rain as Raizo
        - Naomie Harris as Mika Coretti
        - Rick Yune as Takeshi
        - Ben Miles as Ryan Maslow

        Directors:
        - James Marshall

        Producers:
        - Lilly Wachowski
        - Lana Wachowski
        - Joel Silver
        """
    ),

Document(
    title="The Green Mile (1999)",
    content="""Type: Movie
        Title: The Green Mile
        Released: 1999
        Tagline: "Walk a mile you'll never forget."

        Cast:
        - Tom Hanks as Paul Edgecomb
        - Michael Clarke Duncan as John Coffey
        - David Morse as Brutus "Brutal" Howell
        - Bonnie Hunt as Jan Edgecomb
        - James Cromwell as Warden Hal Moores
        - Sam Rockwell as "Wild Bill" Wharton
        - Gary Sinise as Burt Hammersmith
        - Patricia Clarkson as Melinda Moores

        Directors:
        - Frank Darabont
        """
    ),

Document(
    title="Frost/Nixon (2008)",
    content="""Type: Movie
        Title: Frost/Nixon
        Released: 2008
        Tagline: "400 million people were waiting for the truth."

        Cast:
        - Frank Langella as Richard Nixon
        - Michael Sheen as David Frost
        - Kevin Bacon as Jack Brennan
        - Oliver Platt as Bob Zelnick
        - Sam Rockwell as James Reston, Jr.

        Directors:
        - Ron Howard
        """
    ),

Document(
    title="Hoffa (1992)",
    content="""Type: Movie
        Title: Hoffa
        Released: 1992
        Tagline: "He didn't want law. He wanted justice."

        Cast:
        - Jack Nicholson as Hoffa
        - Danny DeVito as Robert "Bobby" Ciaro
        - J.T. Walsh as Frank Fitzsimmons
        - John C. Reilly as Peter "Pete" Connelly

        Directors:
        - Danny DeVito
        """
    ),

Document(
    title="Apollo 13 (1995)",
    content="""Type: Movie
        Title: Apollo 13
        Released: 1995
        Tagline: "Houston, we have a problem."

        Cast:
        - Tom Hanks as Jim Lovell
        - Kevin Bacon as Jack Swigert
        - Ed Harris as Gene Kranz
        - Bill Paxton as Fred Haise
        - Gary Sinise as Ken Mattingly

        Directors:
        - Ron Howard
        """
    ),

Document(
    title="Twister (1996)",
    content="""Type: Movie
        Title: Twister
        Released: 1996
        Tagline: "Don't Breathe. Don't Look Back."

        Cast:
        - Bill Paxton as Bill Harding
        - Helen Hunt as Dr. Jo Harding
        - Zach Grenier as Eddie
        - Philip Seymour Hoffman as Dustin "Dusty" Davis

        Directors:
        - Jan de Bont
        """
    ),

Document(
    title="Cast Away (2000)",
    content="""Type: Movie
        Title: Cast Away
        Released: 2000
        Tagline: "At the edge of the world, his journey begins."

        Cast:
        - Tom Hanks as Chuck Noland
        - Helen Hunt as Kelly Frears

        Directors:
        - Robert Zemeckis
        """
    ),

Document(
    title="One Flew Over the Cuckoo's Nest (1975)",
    content="""Type: Movie
        Title: One Flew Over the Cuckoo's Nest
        Released: 1975
        Tagline: "If he's crazy, what does that make you?"

        Cast:
        - Jack Nicholson as Randle McMurphy
        - Danny DeVito as Martini

        Directors:
        - Milos Forman
        """
    ),

Document(
    title="Something's Gotta Give (2003)",
    content="""Type: Movie
        Title: Something's Gotta Give
        Released: 2003

        Cast:
        - Jack Nicholson as Harry Sanborn
        - Diane Keaton as Erica Barry
        - Keanu Reeves as Julian Mercer

        Directors:
        - Nancy Meyers

        Producers:
        - Nancy Meyers

        Writers:
        - Nancy Meyers
        """
    ),

Document(
    title="Bicentennial Man (1999)",
    content="""Type: Movie
        Title: Bicentennial Man
        Released: 1999
        Tagline: "One robot's 200 year journey to become an ordinary man."

        Cast:
        - Robin Williams as Andrew Marin
        - Oliver Platt as Rupert Burns

        Directors:
        - Chris Columbus
        """
    ),

Document(
    title="Charlie Wilson's War (2007)",
    content="""Type: Movie
        Title: Charlie Wilson's War
        Released: 2007
        Tagline: "A stiff drink. A little mascara. A lot of nerve. Who said they couldn't bring down the Soviet empire."

        Cast:
        - Tom Hanks as Rep. Charlie Wilson
        - Julia Roberts as Joanne Herring
        - Philip Seymour Hoffman as Gust Avrakotos

        Directors:
        - Mike Nichols
        """
    ),

Document(
    title="The Polar Express (2004)",
    content="""Type: Movie
        Title: The Polar Express
        Released: 2004
        Tagline: "This Holiday Season... Believe"

        Cast:
        - Tom Hanks as Hero Boy, Father, Conductor, Hobo, Scrooge, Santa Claus

        Directors:
        - Robert Zemeckis
        """
    ),

Document(
    title="A League of Their Own (1992)",
    content="""Type: Movie
        Title: A League of Their Own
        Released: 1992
        Tagline: "Once in a lifetime you get a chance to do something different."

        Cast:
        - Tom Hanks as Jimmy Dugan
        - Geena Davis as Dottie Hinson
        - Lori Petty as Kit Keller
        - Rosie O'Donnell as Doris Murphy
        - Madonna as "All the Way" Mae Mordabito
        - Bill Paxton as Bob Hinson

        Directors:
        - Penny Marshall
        """
    ),
]



def main():
    # Setup RAG
    embedder = SentenceTransformerEmbedder("BAAI/bge-m3")
    vector_store = ChromaVectorStore(os.getenv("VECTOR_COLLECTION", "rag"))
    rag_service = RAGService(embedder, vector_store)

    # Load documents
    for doc in DOCUMENTS:
        rag_service.add_document(doc.title, doc.content)
    print("Dokumente erfolgreich geladen")

    # Start server
    import core.__main__ as core_main
    setattr(core_main, "rag_service", rag_service)
    core_main.main()

if __name__ == "__main__":
    main()
