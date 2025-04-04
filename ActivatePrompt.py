# ActivatePrompt.py
# Briefly: Renames files with '.prompt' extension to a specified extension
# (.txt, .py, .md) in a target folder, with options for recursion and dry run.
# (c) 2025 Gregory L. Magnusson BANKON license

import os
import sys
import argparse
import logging
from pathlib import Path

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s', stream=sys.stdout)
log = logging.getLogger(__name__)

def rename_prompt_files_final(folder_path_str: str,
                              target_extension: str = ".txt",
                              recursive: bool = False,
                              dry_run: bool = False,
                              assume_yes: bool = False):
    """
    Renames files ending with '.prompt' to the specified target extension
    in the specified folder, optionally recursively.

    Includes dry run, target existence check, and confirmation prompt.

    Args:
        folder_path_str (str): Path to the root folder.
        target_extension (str): The desired new file extension (e.g., ".txt", ".py").
        recursive (bool): If True, process subdirectories recursively.
        dry_run (bool): If True, only prints actions without renaming.
        assume_yes (bool): If True, bypass the confirmation prompt.
    """
    root_path = Path(folder_path_str)
    mode = "[DRY RUN] " if dry_run else ""

    if not target_extension.startswith('.'):
        log.warning(f"Target extension '{target_extension}' should start with a dot. Adding one.")
        target_extension = '.' + target_extension

    log.info(f"{mode}Scanning folder: {root_path.resolve()}")
    log.info(f"{mode}Target extension: '{target_extension}'")
    log.info(f"{mode}Recursive scan: {'Enabled' if recursive else 'Disabled'}")

    if not root_path.is_dir():
        log.error(f"Folder not found at '{folder_path_str}'")
        return

    files_to_rename = []
    skipped_files = []

    try:
        # Determine pattern for glob
        pattern = "**/*.prompt" if recursive else "*.prompt"
        log.info(f"{mode}Searching for files matching: '{pattern}'")

        # Find all matching files first
        for item in root_path.glob(pattern):
            if item.is_file(): # Ensure it's a file
                new_name = item.stem + target_extension
                new_path = item.parent / new_name # Place in the same directory as original

                if new_path.exists():
                    skipped_files.append({'original': item.name, 'target': new_name, 'reason': 'Target exists'})
                else:
                    files_to_rename.append({'old_path': item, 'new_path': new_path})

    except Exception as e:
        log.error(f"An unexpected error occurred while scanning for files: {e}")
        return

    # --- Summary and Confirmation ---
    log.info(f"{mode}Scan complete. Found {len(files_to_rename)} files to rename.")
    if skipped_files:
        log.info(f"{mode}Skipped {len(skipped_files)} files (target already exists).")
        # Optionally list skipped files if needed for debugging
        # for skipped in skipped_files:
        #    log.debug(f"{mode}  - Skipped '{skipped['original']}' because '{skipped['target']}' exists.")

    if not files_to_rename:
        log.info("No files need renaming.")
        return

    # Confirmation prompt (skip if dry_run or assume_yes)
    proceed = False
    if dry_run:
        log.info("Dry run complete. No files were changed.")
        # Show what would be renamed
        for f_info in files_to_rename:
            log.info(f"{mode}Would rename '{f_info['old_path'].name}' to '{f_info['new_path'].name}' in '{f_info['old_path'].parent}'")
        proceed = False # Ensure no renaming happens in dry run
    elif assume_yes:
        log.info("Bypassing confirmation prompt due to --yes flag.")
        proceed = True
    else:
        try:
            confirm = input(f"Proceed with renaming {len(files_to_rename)} files? (yes/no): ").strip().lower()
            if confirm == 'yes':
                proceed = True
            else:
                log.info("Renaming cancelled by user.")
        except EOFError: # Handle case where input stream is closed
             log.info("Renaming cancelled (no input received).")

    # --- Perform Renaming ---
    if proceed:
        log.info("Starting renaming process...")
        renamed_count = 0
        error_count = 0
        for f_info in files_to_rename:
            try:
                f_info['old_path'].rename(f_info['new_path'])
                log.info(f"Renamed '{f_info['old_path'].name}' -> '{f_info['new_path'].name}'")
                renamed_count += 1
            except OSError as e:
                log.error(f"Error renaming '{f_info['old_path'].name}': {e}")
                error_count += 1
            except Exception as e:
                 log.error(f"Unexpected error renaming '{f_info['old_path'].name}': {e}")
                 error_count += 1

        log.info("Renaming process finished.")
        log.info(f"  Successfully renamed: {renamed_count}")
        log.info(f"  Errors during rename: {error_count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Rename files from '.prompt' to a specified extension (default: '.txt').",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog="Examples:\n"
               "  # Rename to .txt in current folder\n"
               "  python ActivatePrompt.py .\n\n"
               "  # Rename to .py recursively in 'prompts' folder (dry run)\n"
               "  python ActivatePrompt.py ./prompts --ext .py --recursive --dry-run\n\n"
               "  # Rename to .md recursively in 'prompts' and execute without prompt\n"
               "  python ActivatePrompt.py ./prompts --ext .md --recursive --yes"
    )
    parser.add_argument(
        "folder_path",
        help="The path to the root folder to scan for .prompt files."
    )
    parser.add_argument(
        "--ext",
        default=".txt",
        help="Target file extension (e.g., .txt, .py, .md). Default: .txt"
    )
    parser.add_argument(
        "-r", "--recursive",
        action="store_true",
        help="Scan subdirectories recursively."
    )
    parser.add_argument(
        "-d", "--dry-run",
        action="store_true",
        help="Simulate the process without renaming files."
    )
    parser.add_argument(
        "-y", "--yes",
        action="store_true",
        help="Bypass the final confirmation prompt."
    )

    args = parser.parse_args()

    rename_prompt_files_final(
        args.folder_path,
        args.ext,
        args.recursive,
        args.dry_run,
        args.yes
    )
