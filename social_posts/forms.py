from django import forms

from .models import Comment, Post, Reply


class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["url", "body", "tags"]
        labels = {"body": "Caption", "label": "Category"}
        widgets = {
            "body": forms.Textarea(
                attrs={
                    "rows": 3,
                    "placeholder": "Add a caption...",
                    "class": "font1 text-4xl",
                }
            ),
            "url": forms.TextInput(
                attrs={
                    "placeholder": "Add url...",
                }
            ),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "id_tags"}),
        }


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["body", "tags"]
        labels = {
            "body": "",
            "tags": "",
        }
        widgets = {
            "body": forms.Textarea(attrs={"rows": 3, "class": "font1 text-4xl"}),
            "tags": forms.CheckboxSelectMultiple(attrs={"class": "id_tags"}),
        }


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(attrs={"placeholder": "Add a comment..."}),
        }
        labels = {"body": ""}


class ReplyCreateForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ["body"]
        widgets = {
            "body": forms.TextInput(
                attrs={"placeholder": "Add a reply...", "class": "text-sm"}
            ),
        }
        labels = {"body": ""}
