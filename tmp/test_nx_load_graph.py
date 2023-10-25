import os
import networkx as nx

# -------------------- CLI arguments -------------------- #
import sys
import argparse

# wrapped program flags
class CLIArguments:
    args: argparse.Namespace

    def __init__(self) -> None:
        self.__log_raw_argv()
        self.__parse_argv()
    
    def __log_raw_argv(self) -> None:
        print("Passed program params:")
        for i in range(len(sys.argv)):
            print("param[{0}]: {1}".format(
                i, sys.argv[i]
            ))
    
    def __parse_argv(self) -> None:
        """
        python main [ARGUMENTS ...]

        Parse program arguments.
            -w max ml workers (threads for ML threads pool, -1 for illimited)
            -d debug
            -fad path to annotated DOT graph directory
            -fa load file containing annotated DOT graph
        """
        parser = argparse.ArgumentParser(description='Program [ARGUMENTS]')
        # file path to annotated DOT graph
        parser.add_argument(
            '-f', 
            '--dot-file-path', 
            type=str, 
            help='File path to annotated DOT graph', 
            required=True
        )

        # save parsed arguments
        self.args = parser.parse_args()

        # log parsed arguments
        print("Parsed program params:")
        for arg in vars(self.args):
            print("{0}: {1}".format(
                arg, getattr(self.args, arg)
            ))

def main(cli: CLIArguments):
    #nx_graph = nx.Graph(nx.nx_pydot.read_dot(annotated_graph_dot_gv_file_path))
    
    # check file exists
    assert os.path.isfile(cli.args.dot_file_path), (
        f"🚩 PANIC: File {cli.args.dot_file_path} does not exist."
    )
    
    # load graph
    nx_graph = nx.Graph(nx.nx_agraph.read_dot(
        cli.args.dot_file_path
    ))

    # check that each node has a 'comment' attribute
    for node, data in nx_graph.nodes(data=True):
        assert 'comment' in data.keys(), (
            f"🚩 PANIC: Node {node} does not have a 'comment' attribute. in graph of file {cli.args.dot_file_path}"
        )
    
    print("👍 All nodes have a 'comment' attribute.")

if __name__ == "__main__":
    cli = CLIArguments()
    main(cli)

