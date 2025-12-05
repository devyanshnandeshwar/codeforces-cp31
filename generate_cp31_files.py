import os
import re
import sys
from textwrap import dedent

# rating -> list of problems (in order)
PROBLEMS = {
    "800": [
        "Halloumi Boxes",
        "Line Trip",
        "Cover in Water",
        "Game with Integers",
        "Jagged Swaps",
        "Doremy's Paint 3",
        "Don't Try to Count",
        "How Much Does Daytona Cost?",
        "Goals of Victory",
        "Target Practice",
        "Ambitious Kid",
        "Sequence Game",
        "United We Stand",
        "Buttons",
        "Array Coloring",
        "Desorting",
        "Forbidden Integer",
        "Grasshopper on a Line",
        "Unit Array",
        "Twin Permutations",
        "Blank Space",
        "Coins",
        "Walking Master",
        "We Need the Zero",
        "Prepend and Append",
        "Serval and Mocha's Array",
        "One and Two",
        "Make it Beautiful",
        "Everybody Likes Good Arrays!",
        "Extremely Round",
        "Two Permutations",
    ],
    "900": [
        "Forked!",
        "Chemistry",
        "Vasilije in Cacak",
        "Jellyfish and Undertale",
        "Make It Zero",
        "Longest Divisors Interval",
        "Balanced Round",
        "Comparison String",
        "Permutation Swap",
        "Odd Queries",
        "Not Dividing",
        "Mainak and Array",
        "NIT Destroys the Universe",
        "AvtoBus",
        "Make It Increasing",
        "Deletive Editing",
        "Array Cloning Technique",
        "Make AP",
        "Odd Grasshopper",
        "AB Balance",
        "Make it Divisible by 25",
        "Luntik and Subsequences",
        "Mocha and Math",
        "Exciting Bets",
        "Bad Boy",
        "Odd Divisor",
        "Strange Partition",
        "Sum of Medians",
        "Three Indices",
        "01 Game",
        "Multiply by 2, divide by 6",
    ],
    "1000": [
        "Swap and Delete",
        "Raspberries",
        "Helmets in Night Light",
        "Olya and Game with Arrays",
        "Monsters",
        "Ski Resort",
        "Array merging",
        "Distinct Split",
        "Minimum LCM",
        "Traffic Light",
        "Basketball Together",
        "Beautiful Array",
        "Luke is a Foodie",
        "Shoe Shuffling",
        "Black and White Stripe",
        "Red Versus Blue",
        "Roof Construction",
        "Triangles on a Rectangle",
        "Divan and a New Project",
        "MEXor Mixup",
        "Double-ended Strings",
        "Add and Divide",
        "Different Divisors",
        "Numbers Box",
        "Valerii Against Everyone",
        "Buying Torches",
        "Fair Numbers",
        "Move Brackets",
        "Johnny and Ancient Computer",
        "Bogosort",
        "Reverse a Substring",
    ],
    "1100": [
        "Erase First or Second Letter",
        "Quests",
        "Collecting Game",
        "Yarik and Array",
        "250 Thousand Tons of TNT",
        "Deja Vu",
        "Building an Aquarium",
        "2D Traveling",
        "Cardboard for Pictures",
        "Tenzing and Books",
        "Maximum Sum",
        "Counting Orders",
        "Lunatic Never Content",
        "Sort the Subarray",
        "JoJo's Incredible Adventures",
        "Subsequence Addition (Hard Version)",
        "Li Hua and Pattern",
        "Teleporters (Easy Version)",
        "Negatives and Positives",
        "GCD Partition",
        "Coprime",
        "Kill Demodogs",
        "Difference of GCDs",
        "AND Sorting",
        "A Perfectly Balanced String?",
        "Eating Candies",
        "Subtract Operation",
        "Fun with Even Subarrays",
        "Paint the Array",
        "Kalindrome Array",
        "Yet Another Card Deck",
    ],
    "1200": [
        "Three Activities",
        "Make Almost Equal With Mod",
        "Plus Minus Permutation",
        "Assembly via Minimums",
        "Vika and the Bridge",
        "Contrast Value",
        "Playing in a Casino",
        "Dora and Search",
        "Matryoshkas",
        "Scuza",
        "Removing Smallest Multiples",
        "Friends and the Restaurant",
        "Virus",
        "Mirror Grid",
        "Binary Deque",
        "Stone Age Problem",
        "Dolce Vita",
        "Differential Sorting",
        "Make Them Equal",
        "Grandma Capa Knits a Scarf",
        "Pleasant Pairs",
        "Stable Groups",
        "Prinzessin der Verurteilung",
        "Palindrome Game (easy version)",
        "Same Differences",
        "AND 0, Sum Big",
        "Flip the Bits",
        "M-Arrays",
        "Cat cycle",
        "Districts Connection",
        "Rock and Lever",
    ],
    "1300": [
        "Divisible Pairs",
        "Find the Different Ones!",
        "Romantic Glasses",
        "Divide and Equalize",
        "Make it Alternating",
        "Strong Vertices",
        "Rudolf and Snowflakes (simple version)",
        "Scoring Subsequences",
        "Gardener and the Array",
        "Yet Another Problem About Pairs Satisfying an Inequality",
        "White-Black Balanced Subtrees",
        "Maximal AND",
        "Chat Ban",
        "Array Elimination",
        "Deep Down Below",
        "Box Fitting",
        "Strange Birthday Party",
        "Move and Turn",
        "Omkar and Last Class of Math",
        "Shuffle",
        "Most socially-distanced subsequence",
        "Buying Shovels",
        "Product of three numbers",
        "Just Eat It!",
        "Balanced Tunnel",
        "WOW Factor",
        "Alyona and a Narrow Fridge",
        "Good Array",
        "Mahmoud and Ehab and the bipartiteness",
        "Average Sleep Time",
        "Simple Strings",
    ],
    "1400": [
        "Anna and the Valentine's Day Gift",
        "Grouping Increases",
        "Jumping Through Segments",
        "Array Game",
        "Dances (Easy version)",
        "Iva & Pav",
        "Bracket Coloring",
        "Copil Copac Draws Trees",
        "Hossam and Friends",
        "Make It Round",
        "Add Modulo 10",
        "Schedule Management",
        "2^Sort",
        "Weird Sum",
        "Fortune Telling",
        "Arranging The Sheep",
        "Berland Regional",
        "AND Sequences",
        "Ball in Berland",
        "Zero Remainder Array",
        "Johnny and Another Rating Drop",
        "Orac and Models",
        "Journey Planning",
        "The Number of Products",
        "Basketball Exercise",
        "Candy Box (easy version)",
        "News Distribution",
        "Lost Numbers",
        "Queen",
        "Tape",
        "Mashmokh and ACM",
    ],
    "1500": [
        "Greetings",
        "Smilo and Monsters",
        "Block Sequence",
        "Data Structures Fan",
        "Tea Tasting",
        "Controllers",
        "Palindrome Basis",
        "Line Empire",
        "Factorials and Powers of Two",
        "AGAGA XOOORRR",
        "Eastern Exhibition",
        "13th Labour of Heracles",
        "Mortal Kombat Tower",
        "k-Amazing Numbers",
        "Balanced Bitstring",
        "Powered Addition",
        "K-Complete Word",
        "Ehab and Path-etic MEXs",
        "Count Subrectangles",
        "Zero Array",
        "Edgy Trees",
        "Zero Quantity Maximization",
        "Lunar New Year and a Wander",
        "Division and Union",
        "The Fair Nut and String",
        "Cut 'em all!",
        "Nested Segments",
        "Minimize the error",
        "Pride",
        "Two TVs",
        "Little Girl and Maximum Sum",
    ],
    "1600": [
        "Partitioning the Array",
        "Good Triples",
        "Decreasing String",
        "To Become Max",
        "Tracking Segments",
        "Round Dance",
        "Hits Different",
        "Shocking Arrangement",
        "Triangle Coloring",
        "Equal Frequencies",
        "Flexible String",
        "Interesting Sequence",
        "Sending a Sequence Over the Network",
        "Meeting on the Line",
        "Split Into Two Sets",
        "Fixed Point Guessing",
        "Maximum Product Strikes Back",
        "Make them Equal",
        "Keshi Is Throwing a Party",
        "Say No to Palindromes",
        "Erase and Extend (Easy Version)",
        "Parsa's Humongous Tree",
        "Planar Reflections",
        "Advertising Agency",
        "Row GCD",
        "Chocolate Bunny",
        "Good Subarrays",
        "Array Walk",
        "Orac and LCM",
        "Linova and Kingdom",
        "Kuroni and Impossible Calculation",
    ],
    "1700": [
        "Maximum modulo equality",
        "Drunken Maze",
        "Tree Pruning",
        "Iris and Game on the Tree",
        "Ruler (hard version)",
        "Swap Dilemma",
        "Beauty of the mountains",
        "Tandem Repeats?",
        "Chat Screenshots",
        "Neutral Tonality",
        "Sum of XOR Functions",
        "Ira and Flamenco",
        "Don't Blame Me",
        "Running Miles",
        "Magic Triples (Easy Version)",
        "Fixed Prefix Permutations",
        "Quiz Master",
        "SlavicG's Favorite Problem",
        "Meta-set",
        "Even Subarrays",
        "Monoblock",
        "Rorororobot",
        "Zero Path",
        "Gambling",
        "Shifting String",
        "Road Optimization",
        "Training Session",
        "The Number of Imposters",
        "Moamen and XOR",
        "Kavi on Pairing Duty",
        "Baby Ehab Partitions Again",
    ],
    "1800": [
        "Gerrymandering",
        "Rendez-vous de Marian et Robin",
        "Money Buys Happiness",
        "Exam in MAC",
        "Bicycles",
        "Kim's Quest",
        "LuoTianyi and the Floating Islands (Easy Version)",
        "A Wide, Wide Graph",
        "Friendly Spiders",
        "Lucky Permutation",
        "Sheikh (Easy version)",
        "Moving Both Hands",
        "Recover an RBS",
        "Max GEQ Sum",
        "Explorer Space",
        "The Sports Festival",
        "Zookeeper and The Infinite Zoo",
        "Road Reform",
        "Apollo versus Pan",
        "The Treasure of The Segments",
        "Catching Cheaters",
        "Identify the Operations",
        "Chef Monocarp",
        "Maximum Distributed Tree",
        "Stoned Game",
        "Count Triangles",
        "Edge Weight Assignment",
        "Three Blocks Palindrome (hard version)",
        "Irreducible Anagrams",
        "Numbers on Tree",
        "Christmas Trees",
    ],
    "1900": [
        "Easy Demon Problem",
        "Recommendations",
        "XORificator 3000",
        "Robin Hood Archery",
        "Yunli's Subarray Queries (easy version)",
        "Longest Max Min Subsequence",
        "Funny Game",
        "Valuable Cards",
        "Non-academic Problem",
        "A BIT of an Inequality",
        "Shuffling Songs",
        "Feed Cats",
        "Good Trip",
        "Blocking Elements",
        "Accumulator Apex",
        "Merge Not Sort",
        "Collapsing Strings",
        "Absolute Beauty",
        "Tree XOR",
        "Tenzing and His Animal Friends",
        "The Butcher",
        "Fish Graph",
        "Hot Start Up (easy version)",
        "Counting Factorizations",
        "Score of a Tree",
        "Restore the Permutation",
        "Yet Another Problem",
        "Divisible Numbers (hard version)",
        "Reset K Edges",
        "2+ doors",
        "River Locks",
    ],
}


def slugify(name: str) -> str:
    """convert problem name to kebab-case for filename"""
    name = name.lower()
    name = re.sub(r"[^a-z0-9]+", "-", name)
    name = name.strip("-")
    return name or "problem"


def make_template(problem_name: str, rating: str, index: int) -> str:
    header = f"""\
    // Codeforces CP31 – Rating {rating} – Problem {index:02d}: {problem_name}
    // Link: https://codeforces.com/   // TODO: add exact link
    // Status: Unsolved / Solved on:   // TODO: update when solved

    """
    body = r"""#include <bits/stdc++.h>
using namespace std;

#define fast_io ios::sync_with_stdio(false); cin.tie(nullptr);

int main() {
    fast_io;

    int T = 1;
    // cin >> T;
    while (T--) {
        // TODO: write solution here
    }

    return 0;
}
"""
    return dedent(header) + body


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # If user passes ratings as args → only generate those
    if args:
        ratings = []
        for r in args:
            if r not in PROBLEMS:
                print(f"Unknown rating {r}, skipping")
            else:
                ratings.append(r)
        if not ratings:
            print("No valid ratings given.")
            return
    else:
        # default: generate for all ratings we have
        ratings = sorted(PROBLEMS.keys(), key=int)

    for rating in ratings:
        problems = PROBLEMS[rating]
        folder = rating
        os.makedirs(folder, exist_ok=True)
        print(f"\n=== Rating {rating} ({len(problems)} problems) ===")
        for i, name in enumerate(problems, start=1):
            slug = slugify(name)
            filename = f"{i:02d}_{slug}.cpp"
            path = os.path.join(folder, filename)

            if os.path.exists(path):
                print(f"Skipped (already exists): {path}")
                continue

            with open(path, "w", encoding="utf-8") as f:
                f.write(make_template(name, rating, i))

            print(f"Created: {path}")

    print("\nDone ✅")


if __name__ == "__main__":
    main()
