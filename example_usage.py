from client import FullstackComponentAstPatchGeneratorClient

def main():
    client = FullstackComponentAstPatchGeneratorClient()
    res = client.generate_ui_component_patch('Dark mode analytics dashboard header with notifications dropdown')
    print('Fullstack Component AST Patch Generator: ' + res['component_patch_id'] + ' (' + res['target_framework'] + ')')
    print('AST Valid: ' + str(res['syntax_ast_valid']) + ' | Files Generated: ' + str(res['generated_code_files_count']))
    print('Live Preview URL: ' + res['live_preview_iframe_url'])
    print('Bundle URL: ' + res['component_source_bundle_url'])

if __name__ == '__main__':
    main()
