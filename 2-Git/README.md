# 1
  ## 1. Create local repository named **lection_git_hw**
    
   ```
   $ git init lection_git_hw
   ```
    
   ![Screenshot_1](screenshots/Screenshot_1.png)

  ## 2. Create file "homework" in this repo and commit it in master branch
    
   ```
   $ touch homework
   $ git add homework
   ```

   ![Screenshot_2](screenshots/Screenshot_2.png)

   ```
   $ git commit -m "Add homework file"
   ```

   ![Screenshot_3](screenshots/Screenshot_3.png)

  ## 3. Create branch "hw_git" and insert anything in the file and commit these changes to this branch
    
   ```
   $ git branch hw_git
   $ git checkout hw_git
   $ echo "This text was added on hw_git branch" >> homework
   ```

   ![Screenshot_4](screenshots/Screenshot_4.png)

   ```
   $ git add homework
   $ git commit -m "Add some test to homework file" 
   ```

   ![Screenshot_5](screenshots/Screenshot_5.png)

   As I made a small mistake in commit text, I want to edit it by next command:

   ```
   $ git commit --amend -m "Add some text to homework file"
   ```

   ![Screenshot_6](screenshots/Screenshot_6.png)

  ## 4. Switch back to master branch and add anything else to the empty file "homework" there too
    
   ```
   $ git checkout master
   $ echo "This text was added on master branch."
   ```

   ![Screenshot_7](screenshots/Screenshot_7.png)

   ```
   $ git add homework
   $ git commit -m "Add some text to homework file"
   ```

  ## 5. Merge branch "hw_git" to "master", keep only changes from "hw_git" branch
    
   ```
   $ git merge hw_git
   ```

   ![Screenshot_8](screenshots/Screenshot_8.png)

   ```
   $ vim homework
   ```

   ![Screenshot_9](screenshots/Screenshot_9.png)

   Leave only changes from **hw_git** branchL

   ![Screenshot_10](screenshots/Screenshot_10.png)

   ```
   $ git add homework
   $ git commit -m "Add some text to homework file"
   $ git merge hw_git
   ```

   ![Screenshot_11](screenshots/Screenshot_11.png)

  ## 6. Switch to "hw_git" branch again and create new file "temp_file" and commit it
    
   ```
   $ git checkout hw_git
   $ touch temp_file
   $ git add temp_file
   $ git commit -m "Add temp_file"
   ```

   ![Screenshot_12](screenshots/Screenshot_12.png)

  ## 7. Revert to the first commit in "hw_git" branch
    
   ```
   $ git log --decorate
   ```

   ![Screenshot_13](screenshots/Screenshot_13.png)

   ```
   $ git checkout 7afed2e
   ```

   ![Screenshot_14](screenshots/Screenshot_14.png)

   There is no *temp_file* , *homework* is empty:

   ![Screenshot_15](screenshots/Screenshot_15.png)

   There is another way to replace HEAD to the first commit in the branch:

   ```
   $ git reset --hard HEAD~2
   ```

   ![Screenshot_17](screenshots/Screenshot_17.png)

   The difference between using **checkout** and **reset** commands is that **checkout** replace HEAD pointer in *detached HEAD* state and **reset** update both HEAD and branch state. 

   **checkout** is considered to be *working-directory safe* as it checks up on files that have been changed and leave them in the working directory.

   There is a great cheat-sheet table in [Git Documetation](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified):

   > The “HEAD” column reads “REF” if that command moves the reference (branch) that HEAD points to, and “HEAD” if it moves HEAD itself. Pay especial attention to the 'WD Safe?' column — if it says NO, take a second to think before running that command.

   ![Cheat-sheet](screenshots/cheat-sheet-revert.png) 

    
# 2
  ## 1. Create empty repository "lection_git_hw" on in Github
  ## 2. Set remote from your local repo from task 1 to this new repo
      
   ```
   $ git remote add origin https://github.com/dahachm/lection_git_hw.git
   ```  

   ![Screenshot_18](screenshots/Screenshot_18.png)

  ## 3. Push all branches to the remote repo
    
   ```
   $ git push -u origin master
   $ git push -u origin hw_git
   ```

   ![Screenshot_19](screenshots/Screenshot_19.png)

   ![Screenshot_20](screenshots/Screenshot_20.png)

  ## 4. Change everything in file "homework" in branch "hw_git" to one line "Hello Github", commit it and push
    
   ```
   $ git checkout hw_git
   $ echo "Hello GitHub" > homework
   $ git add homework
   $ git commit -m "Change content of homework file"
   $ git push -u origin hw_git
   ```
   ![Screenshot_21](screenshots/Screenshot_21.png)

  ## 5. Create Pull Request from branch "hw_git" to the master branch and assign me as reviewer to this merge request

   ![Screenshot_22](screenshots/Screenshot_22.png)

# 3
  ## 1. Set up Gitlab CE in docker container
    
   ```
   $ docker run -d -p 80 -p 22 gitlab/gitlab-ce:latest
   ```

   ![Screenshot_23](screenshots/Screenshot_23.png)

   Configure port forwarding to host machine ports 9080 and 9022 to have access in order to WebUI from host machine's browser: (localhost:9080):

   ![Screenshot_24](screenshots/Screenshot_24.png)

  ## 2. Log in as root
    
   ![Screenshot_25](screenshots/Screenshot_25.png)
   ![Screenshot_26](screenshots/Screenshot_26.png)
   ![Screenshot_27](screenshots/Screenshot_27.png)
    
  ## 3. Create group "hw_git"
    
   ![Screenshot_28](screenshots/Screenshot_28.png)
   ![Screenshot_29](screenshots/Screenshot_29.png)
   ![Screenshot_30](screenshots/Screenshot_30.png)

  ## 4. Create two users: maintainer and developer
    
   ![Screenshot_31](screenshots/Screenshot_31.png)
   ![Screenshot_32](screenshots/Screenshot_32.png)
   ![Screenshot_33](screenshots/Screenshot_33.png)
   ![Screenshot_34](screenshots/Screenshot_34.png)
   ![Screenshot_35](screenshots/Screenshot_35.png)
   ![Screenshot_36](screenshots/Screenshot_36.png)
   ![Screenshot_37](screenshots/Screenshot_37.png)

  ## 5. Add these users to the group and set them proper permissions in the group (maintainer – maintainer, developer – developer)
    
   ![Screenshot_38](screenshots/Screenshot_38.png)
   ![Screenshot_39](screenshots/Screenshot_39.png)
   ![Screenshot_40](screenshots/Screenshot_40.png)
   ![Screenshot_41](screenshots/Screenshot_41.png)
   ![Screenshot_42](screenshots/Screenshot_42.png)

  ## 6. Create new project with any name
    
   ![Screenshot_43](screenshots/Screenshot_43.png)
   ![Screenshot_44](screenshots/Screenshot_44.png)
   ![Screenshot_45](screenshots/Screenshot_45.png)


  ## 7. Create all branches for GitFlow in this project (you can create one feature and one release branch and don't create hotfix branch)
    
   ![Screenshot_46](screenshots/Screenshot_46.png)
   ![Screenshot_47](screenshots/Screenshot_47.png)
   ![Screenshot_48](screenshots/Screenshot_48.png)
   ![Screenshot_49](screenshots/Screenshot_49.png)
   ![Screenshot_50](screenshots/Screenshot_50.png)
   ![Screenshot_51](screenshots/Screenshot_51.png)
   ![Screenshot_52](screenshots/Screenshot_52.png)

  ## 8. Protect master branch to allow only maintainers to merge into it, and restrict all to push there
    
   ![Screenshot_53](screenshots/Screenshot_53.png)
   ![Screenshot_54](screenshots/Screenshot_54.png)
   ![Screenshot_55](screenshots/Screenshot_55.png)
   ![Screenshot_56](screenshots/Screenshot_56.png)

  ## 9. Protect release branches by wildcard (release-* for example) and allow only maintainers to merge into it
    
   ![Screenshot_57](screenshots/Screenshot_57.png)
   ![Screenshot_58](screenshots/Screenshot_58.png)

  ## 10. Protect develop branch to allow everyone to create Merge Request into it
    
   ![Screenshot_59](screenshots/Screenshot_59.png)
   ![Screenshot_60](screenshots/Screenshot_60.png)

  ## 11. Allow anyone do anything in branches like "feature-*"
    
   ![Screenshot_61](screenshots/Screenshot_61.png)
    
  ***
   
   Only owner and maintainer are allowed to delete protected branches (except default one - master) using WebUI:

   ![Screenshot_62](screenshots/Screenshot_62.png)
   ![Screenshot_63](screenshots/Screenshot_63.png)
   ![Screenshot_64](screenshots/Screenshot_64.png)

   Let's test new access settings.

   Try to push into *master* branch by *maintainer* (FAIL):

   ![Screenshot_65](screenshots/Screenshot_65.png)

   Try to push into *feature-#23* (new "feature*" branch) by *developer* (SUCCESS):

   ![Screenshot_66](screenshots/Screenshot_66.png)

   Try to merge *feature-#23* into *release* and push into remote *release* branch by *developer* (FAIL):

   ![Screenshot_67](screenshots/Screenshot_67.png)


# EXTRA
  Add TravisCI to Github repo from the first task and Trigger CI on each commit to any branch.

   .travis.yml:

   ```yml
   language: bash
 
   script:
     - echo "Hello World"
   ```
  
   The result:
    
   ![Screenshot_68](screenshots/Screenshot_68.png)

   ![Screenshot_69](screenshots/Screenshot_69.png)



