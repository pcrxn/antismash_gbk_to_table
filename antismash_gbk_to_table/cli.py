#!/usr/bin/env python
import argparse
from pathlib import Path
from antismash_gbk_to_table.funcs import parse_and_write

parser = argparse.ArgumentParser(description="Parse antismash GenBank files")
parser.add_argument(
    "-i",
    "--input",
    type = str,
    help="Path to GenBank file",
    required=True,
)
parser.add_argument(
    "-o",
    "--output",
    type = str,
    help="File path to write to",
    required=True,
)
parser.add_argument(
    "-a",
    "--append",
    default=False,
    help="numoutfiles file",
    required=False,
    action="store_true",
)

parser.add_argument(
    "--header",
    default=False,
    help="Write column headers?",
    required=False,
    action="store_true",
)

parser.add_argument(
    "-s",
    "--sampleid",
    type = str,
    help="Sample ID to add to output table",
    required=False,
)



def main():
    args = parser.parse_args()
    if Path(args.output).exists() and not args.append:
        raise FileExistsError(Path(args.output))
    parse_and_write(
        gbk_path_list=args.input,
        outpath=args.output,
        sampleid=args.sampleid,
        append=args.append,
        header=args.header,

    )


if __name__ == "__main__":
    main()

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
