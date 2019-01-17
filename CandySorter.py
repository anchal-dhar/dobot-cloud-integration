# Exercise 3
# In this exercise, tasks completed will be :
# - Connect to the lext bot using python script
#   - Send a user message in text form , extract the object label
#   - Send a audio and test 
# - Review the repsone and discuss next steps


import logging
# plumbum is a library for providing cli capabilities to the program
from plumbum import cli

class CandySorter(cli.Application):
    verbose = cli.Flag(["-v", "--verbose"], help = "Enable verbose mode")
    test_phrase = cli.SwitchAttr(["-I", "Specify test phrase like 'dobot pickup jelly bean' , include the string in  quotes"],str)

    @cli.switch("-loglevel", int)
    def set_log_level(self, level):
        #"""Sets the log-level of the logger"""
        logging.root.setLevel(level)
    
    def extractCandyLabelByUser(self, test_phrase):
        # TODO
        print("The Test phrase is :", test_phrase)
        
        return test_phrase
    
    def main(self):
        print("Verbose:", self.verbose)
        extraced_label_from_user_phrase = CandySorter.extractCandyLabelByUser(self, self.test_phrase) 
        print("The Extracted Candy Label is :", extraced_label_from_user_phrase)

if __name__ == "__main__":
    CandySorter.run()