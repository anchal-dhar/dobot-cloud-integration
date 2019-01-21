import logging
from plumbum import cli

class MyCompiler(cli.Application):
    verbose = cli.Flag(["-v", "--verbose"], help = "Enable verbose mode")
    include_dirs = cli.SwitchAttr("-I", list = True, help = "Specify include directories")

    @cli.switch("--loglevel", int)
    def set_log_level(self, level):
        """Sets the log-level of the logger"""
        logging.root.setLevel(level)
        print("Loglevel:", level)

    def main(self, *srcfiles):
        print("Verbose:", self.verbose)
        print("Include dirs:", self.include_dirs)
        print("Compiling:", srcfiles)

if __name__ == "__main__":
    MyCompiler.run()