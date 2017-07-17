# -*- coding: utf-8 -*-
#BEGIN_HEADER
import os
import json

from kb_tophat2.Utils.TopHatUtil import TopHatUtil
#END_HEADER


class kb_tophat2:
    '''
    Module Name:
    kb_tophat2

    Module Description:
    A KBase module: kb_tophat2
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "1.0.0"
    GIT_URL = "https://github.com/Tianhao-Gu/kb_tophat2.git"
    GIT_COMMIT_HASH = "9cadfd7e7b0a7101f1daf5642812d289bf0ab1da"

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.config = config
        self.config['SDK_CALLBACK_URL'] = os.environ['SDK_CALLBACK_URL']
        self.config['KB_AUTH_TOKEN'] = os.environ['KB_AUTH_TOKEN']
        #END_CONSTRUCTOR
        pass


    def run_tophat2_app(self, ctx, params):
        """
        run_tophat2_app: run TopHat2 app
        ref: https://ccb.jhu.edu/software/tophat/manual.shtml
        :param params: instance of type "TopHatInput" (required params:
           input_ref: input reads object (Single/Paired_reads, reads_set,
           sample_set) assembly_or_genome_ref: ref to Assembly, ContigSet, or
           Genome workspace_name: the name of the workspace it gets saved to
           alignment_set_suffix: suffix append to alignment set object name
           alignment_suffix: suffix append to alignment object name optional
           params: reads_condition: condition associated with the input reads
           objec (ignored for sets of samples) num_threads: number of
           processing threads read_mismatches: read mismatch cutoff
           read_gap_length: read gap cutoff read_edit_dist: read edit cutoff
           min_intron_length: minimum intron length max_intron_length:
           maximum intron length min_anchor_length: minimum anchor length
           report_secondary_alignments: use this option to output secondary
           alignments no_coverage_search: use this option to disable the
           coverage-based search for junctions library_type: library type
           (fr-unstranded, fr-firststrand, fr-secondstrand) preset_options:
           alignment preset options (b2-very-fast, b2-fast, b2-sensitive,
           b2-very-sensitive) ref:
           https://ccb.jhu.edu/software/tophat/manual.shtml) -> structure:
           parameter "input_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "assembly_or_genome_ref" of type "obj_ref"
           (An X/Y/Z style reference), parameter "workspace_name" of String,
           parameter "alignment_set_suffix" of String, parameter
           "alignment_suffix" of String, parameter "reads_condition" of
           String, parameter "num_threads" of Long, parameter
           "read_mismatches" of Long, parameter "read_gap_length" of Long,
           parameter "read_edit_dist" of Long, parameter "min_intron_length"
           of Long, parameter "max_intron_length" of Long, parameter
           "min_anchor_length" of Long, parameter
           "report_secondary_alignments" of type "boolean" (A boolean - 0 for
           false, 1 for true. @range (0, 1)), parameter "no_coverage_search"
           of type "boolean" (A boolean - 0 for false, 1 for true. @range (0,
           1)), parameter "library_type" of String, parameter
           "preset_options" of String
        :returns: instance of type "TopHatResult" (result_directory: folder
           path that holds all files generated by run_tophat2_app
           reads_alignment_object_ref: generated Alignment/AlignmentSet
           object reference report_name: report name generated by KBaseReport
           report_ref: report reference generated by KBaseReport) ->
           structure: parameter "result_directory" of String, parameter
           "reads_alignment_object_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "report_name" of String, parameter
           "report_ref" of String
        """
        # ctx is the context object
        # return variables are: returnVal
        #BEGIN run_tophat2_app
        print '--->\nRunning kb_tophat2.run_tophat2_app\nparams:'
        print json.dumps(params, indent=1)

        for key, value in params.iteritems():
            if isinstance(value, basestring):
                params[key] = value.strip()

        tophat_runner = TopHatUtil(self.config)
        returnVal = tophat_runner.run_tophat2_app(params)
        #END run_tophat2_app

        # At some point might do deeper type checking...
        if not isinstance(returnVal, dict):
            raise ValueError('Method run_tophat2_app return value ' +
                             'returnVal is not type dict as required.')
        # return the results
        return [returnVal]
    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
