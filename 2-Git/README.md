## 1
  1. Create local repository named **lection_git_hw**
    
    ```
    $ git init lection_git_hw
    ```

    ![Screenshot_1](/screenshots/screenshot_1.png)

  2. Create file "homework" in this repo and commit it in master branch
    
    ```
    $ touch homework
    $ git add homework
    ```

    ![Screenshot_2](/screenshots/screenshot_2.png)

    ```
    $ git commit -m "Add homework file"
    ```

    ![Screenshot_3](/screenshots/screenshot_3.png)

  3. Create branch "hw_git" and insert anything in the file and commit these changes to this branch
    
    ```
    $ git branch hw_git
    $ git checkout hw_git
    $ echo "This text was added on hw_git branch" >> homework
    ```

    ![Screenshot_4](/screenshots/screenshot_4.png)

    ```
    $ git add homework
    $ git commit -m "Add some test to homework file" 
    ```

    ![Screenshot_5](/screenshots/screenshot_5.png)

    As I made a small mistake in commit text, I want to edit it by next command:

    ```
    $ git commit --amend -m "Add some text to homework file"
    ```

    ![Screenshot_6](/screenshots/screenshot_6.png)

  4. Switch back to master branch and add anything else to the empty file "homework" there too
    
    ```
    $ git checkout master
    $ echo "This text was added on master branch."
    ```

    ![Screenshot_7](/screenshots/screenshot_7.png)

    ```
    $ git add homework
    $ git commit -m "Add some text to homework file"
    ```


  5. Merge branch "hw_git" to "master", keep only changes from "hw_git" branch
    
    ```
    $ git merge hw_git
    ```

    ![Screenshot_8](/screenshots/screenshot_8.png)

    ```
    $ vim homework
    ```

    ![Screenshot_9](/screenshots/screenshot_9.png)

    Leave only changes from **hw_git** branchL

    ![Screenshot_10](/screenshots/screenshot_10.png)

    ```
    $ git add homework
    $ git commit -m "Add some text to homework file"
    $ git merge hw_git
    ```

    ![Screenshot_11](/screenshots/screenshot_11.png)

  6. Switch to "hw_git" branch again and create new file "temp_file" and commit it
    
    ```
    $ git checkout hw_git
    $ touch temp_file
    $ git add temp_file
    $ git commit -m "Add temp_file"
    ```

    ![Screenshot_12](/screenshots/screenshot_12.png)

  7. Revert to the first commit in "hw_git" branch
    
    ```
    $ git log --decorate
    ```

    ![Screenshot_13](/screenshots/screenshot_13.png)

    ```
    $ git checkout 7afed2e
    ```

    ![Screenshot_14](/screenshots/screenshot_14.png)

    There is no *temp_file* , *homework* is empty:

    ![Screenshot_15](/screenshots/screenshot_15.png)

    There is another way to replace HEAD to the first commit in the branch:

    ```
    $ git reset --hard HEAD~2
    ```

    ![Screenshot_17](/screenshots/screenshot_17.png)


    The difference between using **checkout** and **reset** commands is that **checkout** replace HEAD pointer in *detached HEAD* state and **reset** update both HEAD and branch state. 

    **checkout** is considered to be *working-directory safe* as it checks up on files that have been changed and leave them in the working directory.

    There is a great cheat-sheet table in [Git Documetation](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified):

    > The “HEAD” column reads “REF” if that command moves the reference (branch) that HEAD points to, and “HEAD” if it moves HEAD itself. Pay especial attention to the 'WD Safe?' column — if it says NO, take a second to think before running that command.

    ![Cheat-sheet](/screenshots/cheat-sheet-revert.png) 



    
## 2
  1. Create empty repository "lection_git_hw" on in Github
  2. Set remote from your local repo from task 1 to this new repo
      
    ```
    $ git remote add origin https://github.com/dahachm/lection_git_hw.git
    ```  

    ![Screenshot_18](/screenshots/screenshot_18.png)

  3. Push all branches to the remote repo
    
    ```
    $ git push -u origin master
    $ git push -u origin hw_git
    ```

    ![Screenshot_19](/screenshots/screenshot_19.png)

    ![Screenshot_20](/screenshots/screenshot_20.png)


  4. Change everything in file "homework" in branch "hw_git" to one line "Hello Github", commit it and push
    
    ```
    $ git checkout hw_git
    $ echo "Hello GitHub" > homework
    $ git add homework
    $ git commit -m "Change content of homework file"
    $ git push -u origin hw_git
    ```
    ![Screenshot_21](/screenshots/screenshot_21.png)

  5. Create Pull Request from branch "hw_git" to the master branch and assign me as reviewer to this merge request

    ![Screenshot_22](/screenshots/screenshot_22.png)

# 3
  1. Set up Gitlab CE in docker container
    
    ```
    $ docker run -d -p 80 -p 22 gitlab/gitlab-ce:latest
    ```

    ![Screenshot_23](/screenshots/screenshot_23.png)

    Configure port forwarding to host machine ports 9080 and 9022 to have access in order to WebUI from host machine's browser: (localhost:9080):

    ![Screenshot_24](/screenshots/screenshot_24.png)

  2. Log in as root
    
    ![Screenshot_25](/screenshots/screenshot_25.png)
    ![Screenshot_26](/screenshots/screenshot_26.png)
    ![Screenshot_27](/screenshots/screenshot_27.png)
    
  3. Create group "hw_git"
    
    ![Screenshot_28](/screenshots/screenshot_28.png)
    ![Screenshot_29](/screenshots/screenshot_29.png)
    ![Screenshot_30](/screenshots/screenshot_30.png)

  4. Create two users: maintainer and developer
    
    ![Screenshot_31](/screenshots/screenshot_31.png)
    ![Screenshot_32](/screenshots/screenshot_32.png)
    ![Screenshot_33](/screenshots/screenshot_33.png)
    ![Screenshot_34](/screenshots/screenshot_34.png)
    ![Screenshot_35](/screenshots/screenshot_35.png)
    ![Screenshot_36](/screenshots/screenshot_36.png)
    ![Screenshot_37](/screenshots/screenshot_37.png)

  5. Add these users to the group and set them proper permissions in the group (maintainer – maintainer, developer – developer)
    
    ![Screenshot_38](/screenshots/screenshot_38.png)
    ![Screenshot_39](/screenshots/screenshot_39.png)
    ![Screenshot_40](/screenshots/screenshot_40.png)
    ![Screenshot_41](/screenshots/screenshot_41.png)
    ![Screenshot_42](/screenshots/screenshot_42.png)

  6. Create new project with any name
    
    ![Screenshot_43](/screenshots/screenshot_43.png)
    ![Screenshot_44](/screenshots/screenshot_44.png)
    ![Screenshot_45](/screenshots/screenshot_45.png)


  7. Create all branches for GitFlow in this project (you can create one feature and one release branch and don't create hotfix branch)
    
    ![Screenshot_46](/screenshots/screenshot_46.png)
    ![Screenshot_47](/screenshots/screenshot_47.png)
    ![Screenshot_48](/screenshots/screenshot_48.png)
    ![Screenshot_49](/screenshots/screenshot_49.png)
    ![Screenshot_50](/screenshots/screenshot_50.png)
    ![Screenshot_51](/screenshots/screenshot_51.png)
    ![Screenshot_52](/screenshots/screenshot_52.png)

  8. Protect master branch to allow only maintainers to merge into it, and restrict all to push there
    
    ![Screenshot_53](/screenshots/screenshot_53.png)
    ![Screenshot_54](/screenshots/screenshot_54.png)
    ![Screenshot_55](/screenshots/screenshot_55.png)
    ![Screenshot_56](/screenshots/screenshot_56.png)

  9. Protect release branches by wildcard (release-* for example) and allow only maintainers to merge into it
    
    ![Screenshot_57](/screenshots/screenshot_57.png)
    ![Screenshot_58](/screenshots/screenshot_58.png)

  10. Protect develop branch to allow everyone to create Merge Request into it
    
    ![Screenshot_59](/screenshots/screenshot_59.png)
    ![Screenshot_60](/screenshots/screenshot_60.png)

  11. Allow anyone do anything in branches like "feature-*"
    
    ![Screenshot_61](/screenshots/screenshot_61.png)
    
    
    Only owner and maintainer are allowew to delete protected branches (except default one - master) using WebUI:

    ![Screenshot_62](/screenshots/screenshot_62.png)
    ![Screenshot_63](/screenshots/screenshot_63.png)
    ![Screenshot_64](/screenshots/screenshot_64.png)

    Let's test new access settings.

    Attempting to push into *master* branch by *maintainer* (FAIL):

    ![Screenshot_65](/screenshots/screenshot_65.png)

    Attempting to push into *feature-#23* (new "feature*" branch) by *developer* (SUCCESS):

    ![Screenshot_66](/screenshots/screenshot_66.png)

    Attempting to merge *feature-#23* into *release* and push into remote *release* branch by *developer* (FAIL):

    ![Screenshot_67](/screenshots/screenshot_67.png)


# EXTRA
  Add TravisCI to Github repo from the first task and Trigger CI on each commit to any branch.

  .travis.yml:

  ```yml
  language: bash

  script:
    - echo "Hello World"
  ```
  
  The result:
    
    ![Screenshot_68](/screenshots/screenshot_68.png)

    ![Screenshot_69](/screenshots/screenshot_69.png)



